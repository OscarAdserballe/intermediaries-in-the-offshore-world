import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from tqdm import tqdm
import powerlaw
import scipy.stats as stats
from collections import defaultdict
import random

# Set plot style
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

def load_data():
    """Load the necessary data files."""
    # Load the enriched random sample data
    enriched_data_path = Path("enrichment_data/enriched_random_sample_500.csv")
    enriched_df = pd.read_csv(enriched_data_path)
    
    # Load the ICIJ data
    icij_data_path = Path("datasets/ICIJ/data")
    
    # Load the necessary data files
    officers_df = pd.read_csv(icij_data_path / "nodes-officers.csv")
    entities_df = pd.read_csv(icij_data_path / "nodes-entities.csv")
    intermediaries_df = pd.read_csv(icij_data_path / "nodes-intermediaries.csv")
    relationships_df = pd.read_csv(icij_data_path / "relationships.csv")
    
    return enriched_df, officers_df, entities_df, intermediaries_df, relationships_df

def create_intermediary_network(intermediary_ids, officers_df, entities_df, intermediaries_df, relationships_df):
    """
    Create a network centered on specific intermediaries.
    
    Parameters:
    -----------
    intermediary_ids : list
        List of intermediary node IDs
    officers_df : pandas.DataFrame
        DataFrame containing officer data
    entities_df : pandas.DataFrame
        DataFrame containing entity data
    intermediaries_df : pandas.DataFrame
        DataFrame containing intermediary data
    relationships_df : pandas.DataFrame
        DataFrame containing relationship data
        
    Returns:
    --------
    networkx.Graph
        The created network
    """
    # Create the graph
    G = nx.Graph()
    
    # Add intermediary nodes
    intermediary_nodes = set(intermediary_ids)
    for intermediary_id in intermediary_nodes:
        intermediary_data = intermediaries_df[intermediaries_df["node_id"] == intermediary_id]
        if not intermediary_data.empty:
            G.add_node(intermediary_id, node_type="intermediary", **intermediary_data.iloc[0].to_dict())
    
    # Get relationships involving these intermediaries
    intermediary_relationships = relationships_df[
        (relationships_df["node_id_start"].isin(intermediary_nodes)) | 
        (relationships_df["node_id_end"].isin(intermediary_nodes))
    ]
    
    # Extract all related nodes
    all_related_nodes = set()
    all_related_nodes.update(intermediary_relationships["node_id_start"].values)
    all_related_nodes.update(intermediary_relationships["node_id_end"].values)
    
    # Add officer nodes
    officer_mask = officers_df["node_id"].isin(all_related_nodes)
    for _, row in officers_df[officer_mask].iterrows():
        G.add_node(row["node_id"], node_type="officer", **row.to_dict())
    
    # Add entity nodes
    entity_mask = entities_df["node_id"].isin(all_related_nodes)
    for _, row in entities_df[entity_mask].iterrows():
        G.add_node(row["node_id"], node_type="entity", **row.to_dict())
    
    # Add edges
    for _, row in intermediary_relationships.iterrows():
        if (row["node_id_start"] in G.nodes) and (row["node_id_end"] in G.nodes):
            G.add_edge(row["node_id_start"], row["node_id_end"], **row.to_dict())
    
    return G

def fit_power_law(data, xmin=None, discrete=True):
    """
    Fit a power law to the data.
    
    Parameters:
    -----------
    data : list or numpy.array
        The data to fit
    xmin : int, optional
        The minimum value to consider
    discrete : bool
        Whether the data is discrete
        
    Returns:
    --------
    powerlaw.Fit
        The fitted power law
    """
    # Filter out zeros and negative values
    data = [x for x in data if x > 0]
    
    if not data:
        return None
    
    # Fit the power law
    try:
        fit = powerlaw.Fit(data, xmin=xmin, discrete=discrete)
        return fit
    except:
        return None

def analyze_degree_distributions_by_classification():
    """Analyze degree distributions by intermediary classification."""
    # Load data
    print("Loading data...")
    enriched_df, officers_df, entities_df, intermediaries_df, relationships_df = load_data()
    
    # Filter for high confidence classifications
    enriched_df = enriched_df[enriched_df["confidence"] == "High"]
    
    # Group intermediaries by classification
    classifications = enriched_df["classification"].unique()
    
    # Create a dictionary to store networks and degree distributions
    networks = {}
    degree_distributions = {}
    power_law_fits = {}
    
    # Create networks and calculate degree distributions for each classification
    print("Creating networks and calculating degree distributions...")
    for classification in tqdm(classifications):
        # Get intermediary IDs for this classification
        intermediary_ids = enriched_df[enriched_df["classification"] == classification]["name"].tolist()
        
        # Create a mapping from name to node_id
        name_to_id = {}
        for _, row in intermediaries_df.iterrows():
            if row["name"] in intermediary_ids:
                name_to_id[row["name"]] = row["node_id"]
        
        # Get node IDs
        node_ids = [name_to_id[name] for name in intermediary_ids if name in name_to_id]
        
        if not node_ids:
            print(f"No intermediaries found for classification: {classification}")
            continue
        
        # Create network
        G = create_intermediary_network(node_ids, officers_df, entities_df, intermediaries_df, relationships_df)
        networks[classification] = G
        
        # Calculate degree distribution
        degrees = [G.degree(n) for n in G.nodes() if G.nodes[n]["node_type"] == "intermediary"]
        degree_distributions[classification] = degrees
        
        # Fit power law
        fit = fit_power_law(degrees)
        power_law_fits[classification] = fit
    
    # Visualize degree distributions
    print("Visualizing degree distributions...")
    for classification in classifications:
        if classification not in degree_distributions or not degree_distributions[classification]:
            continue
        
        plt.figure(figsize=(12, 8))
        
        # Plot degree distribution
        degrees = degree_distributions[classification]
        plt.hist(degrees, bins=20, alpha=0.7, label="Observed")
        
        # Plot power law fit
        fit = power_law_fits[classification]
        if fit:
            # Generate power law data
            x = np.linspace(min(degrees), max(degrees), 100)
            y = fit.power_law.pdf(x) * len(degrees) * (max(degrees) - min(degrees)) / 20
            plt.plot(x, y, 'r-', linewidth=2, label=f"Power Law (α={fit.alpha:.2f})")
            
            # Print power law parameters
            print(f"\nPower Law Fit for {classification}:")
            print(f"Alpha: {fit.alpha:.2f}")
            print(f"Xmin: {fit.xmin:.2f}")
            print(f"KS statistic: {fit.KS:.4f}")
            print(f"P-value: {fit.p:.4f}")
            
            # Test if power law is a good fit
            if fit.p > 0.1:
                print("Power law is a good fit (p > 0.1)")
            else:
                print("Power law is not a good fit (p <= 0.1)")
        
        plt.title(f"Degree Distribution for {classification} Intermediaries")
        plt.xlabel("Degree")
        plt.ylabel("Count")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f"output/powerlaw_{classification.replace(' ', '_')}.png")
        plt.show()
    
    # Create a summary table
    summary_data = []
    for classification in classifications:
        if classification not in power_law_fits or not power_law_fits[classification]:
            continue
        
        fit = power_law_fits[classification]
        summary_data.append({
            "Classification": classification,
            "Alpha": fit.alpha,
            "Xmin": fit.xmin,
            "KS statistic": fit.KS,
            "P-value": fit.p,
            "Good fit": fit.p > 0.1,
            "Sample size": len(degree_distributions[classification])
        })
    
    summary_df = pd.DataFrame(summary_data)
    summary_df.to_csv("output/powerlaw_summary.csv", index=False)
    print("\nSummary saved to output/powerlaw_summary.csv")
    
    return networks, degree_distributions, power_law_fits

def compare_with_random_removal():
    """Compare targeted removal of high-degree intermediaries with random removal."""
    # Load data
    print("Loading data...")
    enriched_df, officers_df, entities_df, intermediaries_df, relationships_df = load_data()
    
    # Filter for high confidence classifications
    enriched_df = enriched_df[enriched_df["confidence"] == "High"]
    
    # Create a network with all intermediaries
    print("Creating network...")
    intermediary_ids = enriched_df["name"].tolist()
    
    # Create a mapping from name to node_id
    name_to_id = {}
    for _, row in intermediaries_df.iterrows():
        if row["name"] in intermediary_ids:
            name_to_id[row["name"]] = row["node_id"]
    
    # Get node IDs
    node_ids = [name_to_id[name] for name in intermediary_ids if name in name_to_id]
    
    # Create network
    G = create_intermediary_network(node_ids, officers_df, entities_df, intermediaries_df, relationships_df)
    
    # Get intermediary nodes
    intermediary_nodes = [n for n, d in G.nodes(data=True) if d.get("node_type") == "intermediary"]
    
    # Calculate initial network metrics
    initial_components = list(nx.connected_components(G))
    initial_largest_cc_size = len(max(initial_components, key=len))
    initial_num_components = len(initial_components)
    
    print(f"Initial network: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    print(f"Initial largest component: {initial_largest_cc_size} nodes")
    print(f"Initial number of components: {initial_num_components}")
    
    # Simulate targeted removal of high-degree intermediaries
    print("\nSimulating targeted removal...")
    G_targeted = G.copy()
    intermediary_nodes_targeted = [n for n, d in G_targeted.nodes(data=True) if d.get("node_type") == "intermediary"]
    
    # Sort intermediaries by degree
    intermediary_degrees = [(n, G_targeted.degree(n)) for n in intermediary_nodes_targeted]
    intermediary_degrees.sort(key=lambda x: x[1], reverse=True)
    
    # Remove top 10% of intermediaries by degree
    num_to_remove = max(1, int(len(intermediary_degrees) * 0.1))
    nodes_to_remove = [n for n, _ in intermediary_degrees[:num_to_remove]]
    
    G_targeted.remove_nodes_from(nodes_to_remove)
    
    # Calculate network metrics after targeted removal
    targeted_components = list(nx.connected_components(G_targeted))
    targeted_largest_cc_size = len(max(targeted_components, key=len))
    targeted_num_components = len(targeted_components)
    
    print(f"After targeted removal: {G_targeted.number_of_nodes()} nodes, {G_targeted.number_of_edges()} edges")
    print(f"Largest component: {targeted_largest_cc_size} nodes")
    print(f"Number of components: {targeted_num_components}")
    
    # Simulate random removal of intermediaries
    print("\nSimulating random removal...")
    G_random = G.copy()
    intermediary_nodes_random = [n for n, d in G_random.nodes(data=True) if d.get("node_type") == "intermediary"]
    
    # Randomly select intermediaries to remove
    random.shuffle(intermediary_nodes_random)
    nodes_to_remove = intermediary_nodes_random[:num_to_remove]
    
    G_random.remove_nodes_from(nodes_to_remove)
    
    # Calculate network metrics after random removal
    random_components = list(nx.connected_components(G_random))
    random_largest_cc_size = len(max(random_components, key=len))
    random_num_components = len(random_components)
    
    print(f"After random removal: {G_random.number_of_nodes()} nodes, {G_random.number_of_edges()} edges")
    print(f"Largest component: {random_largest_cc_size} nodes")
    print(f"Number of components: {random_num_components}")
    
    # Compare results
    print("\nComparison:")
    print(f"Targeted removal reduced largest component by {(initial_largest_cc_size - targeted_largest_cc_size) / initial_largest_cc_size:.2%}")
    print(f"Random removal reduced largest component by {(initial_largest_cc_size - random_largest_cc_size) / initial_largest_cc_size:.2%}")
    print(f"Targeted removal increased number of components by {(targeted_num_components - initial_num_components) / initial_num_components:.2%}")
    print(f"Random removal increased number of components by {(random_num_components - initial_num_components) / initial_num_components:.2%}")
    
    # Visualize the results
    plt.figure(figsize=(12, 8))
    
    # Plot largest component size
    plt.subplot(2, 1, 1)
    plt.bar(["Initial", "Targeted Removal", "Random Removal"], 
            [initial_largest_cc_size, targeted_largest_cc_size, random_largest_cc_size])
    plt.title("Largest Component Size")
    plt.ylabel("Number of Nodes")
    
    # Plot number of components
    plt.subplot(2, 1, 2)
    plt.bar(["Initial", "Targeted Removal", "Random Removal"], 
            [initial_num_components, targeted_num_components, random_num_components])
    plt.title("Number of Components")
    plt.ylabel("Count")
    
    plt.tight_layout()
    plt.savefig("output/removal_comparison.png")
    plt.show()
    
    return G, G_targeted, G_random

if __name__ == "__main__":
    # Create output directory if it doesn't exist
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # Analyze degree distributions by classification
    networks, degree_distributions, power_law_fits = analyze_degree_distributions_by_classification()
    
    # Compare targeted vs random removal
    G, G_targeted, G_random = compare_with_random_removal()
    
    print("Analysis complete!") 