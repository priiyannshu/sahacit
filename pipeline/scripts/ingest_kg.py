"""
Master KG Ingestion Script
Parses 3 knowledge graphs, extracts nodes + edges,
embeds locally via BGE Base, outputs NDJSON for Vectorize + JSON for D1.

Subjects: polity (Indian Constitution), philosophy (InPhO), cs (ConceptNet)
"""

import json
import sys
import os
import re
import time
from pathlib import Path

# Suppress rdflib date warnings
import warnings
warnings.filterwarnings("ignore")

import rdflib
from rdflib import RDF, RDFS, OWL, Namespace

ROOT = Path(__file__).parent.parent
OUTPUT = ROOT / "data" / "kg" / "output"
OUTPUT.mkdir(exist_ok=True)


# ─────────────────────────────────────────────
# 1. INDIAN CONSTITUTION (polity)
# ─────────────────────────────────────────────

def extract_polity():
    """Extract nodes + edges from indianconstitution package."""
    from indianconstitution import get_constitution
    from indianconstitution.core.engine import ConstitutionGraph

    ic = get_constitution()
    cg = ConstitutionGraph(ic.data.articles)
    g = cg.graph

    nodes = []
    edges = []

    # Well-known parts of the Indian Constitution (article ranges)
    PART_MAP = {
        (1, 4): "Part I - The Union and its Territory",
        (5, 11): "Part II - Citizenship",
        (12, 35): "Part III - Fundamental Rights",
        (36, 51): "Part IV - Directive Principles",
        (51, 51): "Part IV - Directive Principles",
        (52, 58): "Part V - The Union",
        (58, 72): "Part V - The Union",
        (73, 76): "Part V - The Union",
        (77, 95): "Part V - The Union",
        (96, 112): "Part V - The Union",
        (112, 151): "Part V - The Union",
        (151, 151): "Part V - The Union",
        (152, 167): "Part VI - The States",
        (168, 177): "Part VI - The States",
        (178, 187): "Part VI - The States",
        (188, 188): "Part VI - The States",
        (189, 200): "Part VI - The States",
        (201, 201): "Part VI - The States",
        (202, 207): "Part VI - The States",
        (208, 212): "Part VI - The States",
        (213, 213): "Part VI - The States",
        (214, 231): "Part VI - The States",
        (232, 237): "Part VI - The States",
        (238, 238): "Part VI - The States",
        (239, 241): "Part VII - States in Part B of the First Schedule",
        (242, 243): "Part VII - States in Part B of the First Schedule",
        (243, 243): "Part VIII - Union Territories",
        (244, 244): "Part VIII - Union Territories",
        (244, 244): "Part VIII - Union Territories",
        (245, 263): "Part IX - The Panchayats",
        (264, 264): "Part IX - The Panchayats",
        (265, 275): "Part IXA - The Municipalities",
        (276, 276): "Part IXA - The Municipalities",
        (277, 278): "Part IXB - The Co-operative Societies",
        (279, 279): "Part IXB - The Co-operative Societies",
        (280, 289): "Part X - Scheduled and Tribal Areas",
        (290, 291): "Part X - Scheduled and Tribal Areas",
        (292, 293): "Part XI - Relations between the Union and the States",
        (294, 300): "Part XI - Relations between the Union and the States",
        (301, 307): "Part XI - Relations between the Union and the States",
        (308, 323): "Part XI - Relations between the Union and the States",
        (324, 329): "Part XII - Finance, Property, Contracts and Suits",
        (330, 342): "Part XII - Finance, Property, Contracts and Suits",
        (343, 344): "Part XII - Finance, Property, Contracts and Suits",
        (345, 345): "Part XII - Finance, Property, Contracts and Suits",
        (346, 347): "Part XII - Finance, Property, Contracts and Suits",
        (348, 348): "Part XII - Finance, Property, Contracts and Suits",
        (349, 351): "Part XII - Finance, Property, Contracts and Suits",
        (352, 360): "Part XIII - Trade, Commerce and Intercourse",
        (361, 367): "Part XIII - Trade, Commerce and Intercourse",
        (368, 368): "Part XIV - Services under the Union and the States",
        (369, 370): "Part XIV - Services under the Union and the States",
        (370, 370): "Part XIV - Services under the Union and the States",
        (371, 371): "Part XIV - Services under the Union and the States",
        (372, 378): "Part XIV - Services under the Union and the States",
        (379, 387): "Part XIV - Services under the Union and the States",
        (388, 392): "Part XIV - Services under the Union and the States",
        (393, 393): "Part XIV - Services under the Union and the States",
        (394, 394): "Part XIV - Services under the Union and the States",
        (395, 395): "Part XIV - Services under the Union and the States",
        (396, 398): "Part XIV - Services under the Union and the States",
        (399, 399): "Part XIV - Services under the Union and the States",
        (400, 400): "Part XIV - Services under the Union and the States",
        (401, 401): "Part XIV - Services under the Union and the States",
        (402, 402): "Part XIV - Services under the Union and the States",
        (403, 403): "Part XIV - Services under the Union and the States",
        (404, 404): "Part XIV - Services under the Union and the States",
        (405, 405): "Part XIV - Services under the Union and the States",
        (406, 406): "Part XIV - Services under the Union and the States",
        (407, 407): "Part XIV - Services under the Union and the States",
        (408, 408): "Part XIV - Services under the Union and the States",
        (409, 409): "Part XIV - Services under the Union and the States",
        (410, 410): "Part XIV - Services under the Union and the States",
        (411, 411): "Part XIV - Services under the Union and the States",
        (412, 412): "Part XIV - Services under the Union and the States",
        (413, 413): "Part XIV - Services under the Union and the States",
        (414, 414): "Part XIV - Services under the Union and the States",
        (415, 415): "Part XIV - Services under the Union and the States",
        (416, 416): "Part XIV - Services under the Union and the States",
        (417, 417): "Part XIV - Services under the Union and the States",
        (418, 418): "Part XIV - Services under the Union and the States",
        (419, 419): "Part XIV - Services under the Union and the States",
        (420, 420): "Part XIV - Services under the Union and the States",
        (421, 421): "Part XIV - Services under the Union and the States",
        (422, 422): "Part XIV - Services under the Union and the States",
        (423, 423): "Part XIV - Services under the Union and the States",
        (424, 424): "Part XIV - Services under the Union and the States",
        (425, 425): "Part XIV - Services under the Union and the States",
        (426, 426): "Part XIV - Services under the Union and the States",
        (427, 427): "Part XIV - Services under the Union and the States",
        (428, 428): "Part XIV - Services under the Union and the States",
        (429, 429): "Part XIV - Services under the Union and the States",
        (430, 430): "Part XIV - Services under the Union and the States",
        (431, 431): "Part XIV - Services under the Union and the States",
        (432, 432): "Part XIV - Services under the Union and the States",
        (433, 433): "Part XIV - Services under the Union and the States",
        (434, 434): "Part XIV - Services under the Union and the States",
        (435, 435): "Part XIV - Services under the Union and the States",
        (436, 436): "Part XIV - Services under the Union and the States",
        (437, 437): "Part XIV - Services under the Union and the States",
        (438, 438): "Part XIV - Services under the Union and the States",
        (439, 439): "Part XIV - Services under the Union and the States",
        (440, 440): "Part XIV - Services under the Union and the States",
        (441, 441): "Part XIV - Services under the Union and the States",
        (442, 442): "Part XIV - Services under the Union and the States",
        (443, 443): "Part XIV - Services under the Union and the States",
        (444, 444): "Part XIV - Services under the Union and the States",
        (445, 445): "Part XIV - Services under the Union and the States",
        (446, 446): "Part XIV - Services under the Union and the States",
        (447, 447): "Part XIV - Services under the Union and the States",
        (448, 448): "Part XIV - Services under the Union and the States",
        (449, 449): "Part XIV - Services under the Union and the States",
        (450, 450): "Part XIV - Services under the Union and the States",
        (451, 451): "Part XIV - Services under the Union and the States",
        (452, 452): "Part XIV - Services under the Union and the States",
        (453, 453): "Part XIV - Services under the Union and the States",
        (454, 454): "Part XIV - Services under the Union and the States",
        (455, 455): "Part XIV - Services under the Union and the States",
        (456, 456): "Part XIV - Services under the Union and the States",
        (457, 457): "Part XIV - Services under the Union and the States",
        (458, 458): "Part XIV - Services under the Union and the States",
        (459, 459): "Part XIV - Services under the Union and the States",
        (460, 460): "Part XIV - Services under the Union and the States",
        (461, 461): "Part XIV - Services under the Union and the States",
        (462, 462): "Part XIV - Services under the Union and the States",
        (463, 463): "Part XIV - Services under the Union and the States",
        (464, 464): "Part XIV - Services under the Union and the States",
    }

    # Better: use well-known constitutional parts
    def get_part(num_str):
        # Extract numeric part from article number (e.g., "21A" -> 21)
        m = re.match(r'(\d+)', str(num_str))
        num = int(m.group(1)) if m else 0
        if num <= 4: return "Part I - Union and Territory"
        if num <= 11: return "Part II - Citizenship"
        if num <= 51: return "Part III - Fundamental Rights" if num <= 35 else "Part IV - Directive Principles"
        if num <= 151: return "Part V - The Union"
        if num <= 237: return "Part VI - The States"
        if num <= 238: return "Part VII - States in Part B"
        if num <= 242: return "Part VIII - Union Territories"
        if num <= 243: return "Part IX - The Panchayats"
        if num <= 263: return "Part IXA - The Municipalities"
        if num <= 278: return "Part IXB - Co-operative Societies"
        if num <= 289: return "Part X - Scheduled and Tribal Areas"
        if num <= 291: return "Part XI - Union-State Relations"
        if num <= 307: return "Part XI - Union-State Relations"
        if num <= 323: return "Part XI - Union-State Relations"
        if num <= 351: return "Part XII - Finance, Property, Contracts"
        if num <= 367: return "Part XIII - Trade and Commerce"
        if num <= 370: return "Part XIV - Services"
        if num <= 391: return "Part XIVA - Tribunals"
        if num <= 395: return "Part XV - Elections"
        if num <= 396: return "Part XVI - Special Provisions"
        if num <= 400: return "Part XVII - Official Language"
        if num <= 407: return "Part XVIII - Emergency Provisions"
        if num <= 412: return "Part XIX - Miscellaneous"
        if num <= 420: return "Part XX - Amendment"
        if num <= 421: return "Part XXI - Temporary and Transitional"
        if num <= 422: return "Part XXII - Short title, commencement"
        return "Constitution"

    for art in ic.data.articles:
        num_str = str(art.number)
        node_id = f"polity_art_{num_str}"
        topic = get_part(num_str)
        content = art.content.strip() if art.content else ""
        summary = content[:500] if content else art.title

        nodes.append({
            "id": node_id,
            "subject": "polity",
            "topic": topic,
            "title": f"Article {art.number}: {art.title}",
            "summary": summary,
            "canonical_facts": [content] if content else [],
        })

    # Cross-reference edges
    for u, v, _ in g.edges(data=True):
        edges.append({
            "source_id": f"polity_art_{u}",
            "target_id": f"polity_art_{v}",
            "relation": "cross_references",
        })

    print(f"  Polity: {len(nodes)} nodes, {len(edges)} edges")
    return nodes, edges


# ─────────────────────────────────────────────
# 2. InPhO (philosophy)
# ─────────────────────────────────────────────

def extract_philosophy():
    """Extract nodes + edges from InPhO OWL."""
    g = rdflib.Graph()
    g.parse(str(ROOT / "kg" / "inpho" / "inpho.owl"))

    nodes = []
    edges = []
    seen = set()

    # Types we care about
    VALUE_TYPES = {
        "Thinker", "Idea", "Journal",
        "Idea_in_Epistemology", "Idea_in_Ethics", "Idea_in_Logic_and_Language",
        "Idea_in_Metaphysics", "Idea_in_Philosophy_of_Mind",
        "Idea_in_Social_and_Political_Philosophy", "Idea_in_Aesthetics",
        "Idea_in_Philosophy_of_Science", "Idea_in_History_of_Philosophy",
        "Idea_in_Philosophy_of_Religion", "Idea_in_Moral_Epistemology_and_Moral_Reasoning",
        "Idea_about_Issues_in_Social_Justice",
    }
    # Anything starting with "Idea_" is good
    def is_useful_type(type_uri):
        local = str(type_uri).split("#")[-1].split("/")[-1]
        return local in VALUE_TYPES or local.startswith("Idea_") or local in {"Thinker", "Journal"}

    # Build class hierarchy for understanding
    class_labels = {}
    for s, p, o in g.triples((None, RDFS.label, None)):
        class_labels[str(s)] = str(o)

    # Extract instances
    for s, p, o in g.triples((None, RDF.type, None)):
        type_str = str(o).split("#")[-1].split("/")[-1]
        if not is_useful_type(o):
            continue

        uri = str(s)
        if uri in seen:
            continue
        seen.add(uri)

        local = uri.split("#")[-1].split("/")[-1]
        label = class_labels.get(uri, local.replace("_", " "))

        # Get additional properties
        influences = []
        for _, _, inf in g.triples((s, None, None)):
            pred = str(_).split("#")[-1].split("/")[-1] if _ else ""
            if "influenced" in pred.lower():
                inf_local = str(inf).split("#")[-1].split("/")[-1]
                influences.append(inf_local)

        # Determine subject: philosophers are philosophy, ideas are philosophy
        subject = "philosophy"

        # Create a descriptive summary
        summary_parts = [f"{label}"]
        if type_str == "Thinker":
            # Get nationality, profession, birth/death
            for _, pred, val in g.triples((s, None, None)):
                pred_local = str(pred).split("#")[-1].split("/")[-1]
                if pred_local == "has_nationality":
                    summary_parts.append(f"Nationality: {val}")
                elif pred_local == "has_birthdate":
                    summary_parts.append(f"Born: {val}")
                elif pred_local == "has_deathdate":
                    summary_parts.append(f"Died: {val}")

        node_id = f"phil_{local}".lower().replace(" ", "_").replace("-", "_")[:80]

        # Clean the summary
        summary = ". ".join(summary_parts)

        nodes.append({
            "id": node_id,
            "subject": subject,
            "topic": type_str.replace("Idea_in_", "").replace("Idea_about_", "").replace("_", " "),
            "title": label,
            "summary": summary,
            "canonical_facts": [f"{label} is a {type_str.replace('_', ' ').lower()}"],
        })

    # Deduplicate nodes by id
    node_map = {}
    for n in nodes:
        if n["id"] not in node_map:
            node_map[n["id"]] = n
    nodes = list(node_map.values())
    node_ids = set(node_map.keys())

    # Extract edges: has_influenced relationships
    INFLUENCE_PRED = None
    for s, p, o in g:
        pred_local = str(p).split("#")[-1].split("/")[-1]
        if pred_local == "has_influenced":
            INFLUENCE_PRED = p
            break

    if INFLUENCE_PRED:
        for s, p, o in g.triples((None, INFLUENCE_PRED, None)):
            src = str(s).split("#")[-1].split("/")[-1]
            tgt = str(o).split("#")[-1].split("/")[-1]
            src_id = f"phil_{src}".lower().replace(" ", "_").replace("-", "_")[:80]
            tgt_id = f"phil_{tgt}".lower().replace(" ", "_").replace("-", "_")[:80]
            if src_id in node_ids and tgt_id in node_ids:
                edges.append({
                    "source_id": src_id,
                    "target_id": tgt_id,
                    "relation": "influenced",
                })
    else:
        print("  Warning: No has_influenced predicate found in InPhO")

    print(f"  Philosophy: {len(nodes)} nodes, {len(edges)} edges")
    return nodes, edges


# ─────────────────────────────────────────────
# 3. CONCEPTNET (cs / commonsense)
# ─────────────────────────────────────────────

def extract_cs():
    """Extract CS/AI concepts as seed nodes. Edges will come from semantic embedding."""
    SEED_CONCEPTS = [
        "algorithm", "data structure", "machine learning", "artificial intelligence",
        "neural network", "deep learning", "natural language processing",
        "computer vision", "optimization", "complexity theory",
        "database", "operating system", "computer network", "cryptography",
        "software engineering", "compiler", "parallel computing",
        "distributed system", "graph theory", "automata theory",
        "programming language", "object oriented programming",
        "functional programming", "recursion", "dynamic programming",
        "binary search", "hash table", "linked list", "tree", "graph",
        "sorting algorithm", "search algorithm", "greedy algorithm",
        "backtracking", "divide and conquer", "breadth first search",
        "depth first search", "dijkstra", "bellman ford",
        "reinforcement learning", "supervised learning", "unsupervised learning",
        "convolutional neural network", "recurrent neural network",
        "transformer", "attention mechanism", "gradient descent",
        "backpropagation", "loss function", "activation function",
        "overfitting", "regularization", "cross validation",
        "precision", "recall", "f1 score", "confusion matrix",
        "decision tree", "random forest", "support vector machine",
        "k nearest neighbors", "naive bayes", "logistic regression",
        "linear regression", "pca", "dimensionality reduction",
        "clustering", "k means", "hierarchical clustering",
        "information theory", "entropy", "mutual information",
        "turing machine", "halting problem", "p vs np",
        "big o notation", "time complexity", "space complexity",
        "stack", "queue", "heap", "priority queue",
        "binary tree", "binary search tree", "red black tree",
        "avl tree", "b tree", "trie",
        "bloom filter", "hash function", "collision",
        "deadlock", "semaphore", "mutex", "thread", "process",
        "virtual memory", "paging", "segmentation",
        "tcp", "udp", "http", "dns", "ip address",
        "router", "switch", "firewall", "load balancer",
        "relational database", "sql", "normalization", "index",
        "transaction", "acid", "cap theorem",
        "api", "rest", "microservices", "serverless",
        "container", "docker", "kubernetes",
        "version control", "git", "continuous integration",
        "agile", "scrum", "waterfall",
        "software testing", "unit test", "integration test",
        "design pattern", "singleton", "factory", "observer",
        "solid principles", "dependency injection",
        "lambda calculus", "type theory", "formal verification",
        "model checking", "theorem proving",
        "quantum computing", "qubit", "quantum entanglement",
        "blockchain", "distributed ledger", "consensus algorithm",
        "cybersecurity", "authentication", "authorization",
        "encryption", "decryption", "digital signature",
    ]

    nodes = []
    edges = []
    seen_concepts = set()

    for concept in SEED_CONCEPTS:
        node_id = f"cs_{concept.replace(' ', '_').lower()}"
        if node_id in seen_concepts:
            continue
        seen_concepts.add(node_id)

        nodes.append({
            "id": node_id,
            "subject": "cs",
            "topic": "Computer Science",
            "title": concept.title(),
            "summary": f"A concept in computer science: {concept}",
            "canonical_facts": [f"{concept} is a concept in computer science and artificial intelligence"],
        })

    # Edges will be computed from semantic embeddings (cross-subject semantic edges)
    print(f"  CS: {len(nodes)} nodes, {len(edges)} edges (edges from embeddings)")
    return nodes, edges


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    print("=" * 60)
    print("KG Ingestion Pipeline")
    print("=" * 60)

    all_nodes = []
    all_edges = []

    print("\n[1/3] Extracting Polity (Indian Constitution)...")
    polity_nodes, polity_edges = extract_polity()
    all_nodes.extend(polity_nodes)
    all_edges.extend(polity_edges)

    print("\n[2/3] Extracting Philosophy (InPhO)...")
    phil_nodes, phil_edges = extract_philosophy()
    all_nodes.extend(phil_nodes)
    all_edges.extend(phil_edges)

    print("\n[3/3] Extracting CS/AI (ConceptNet)...")
    cs_nodes, cs_edges = extract_cs()
    all_nodes.extend(cs_nodes)
    all_edges.extend(cs_edges)

    # ── Save raw node + edge data ──
    print(f"\n{'=' * 60}")
    print(f"TOTAL: {len(all_nodes)} nodes, {len(all_edges)} edges")

    with open(OUTPUT / "all_nodes.json", "w") as f:
        json.dump(all_nodes, f, indent=2)
    with open(OUTPUT / "all_edges.json", "w") as f:
        json.dump(all_edges, f, indent=2)
    print(f"Saved to {OUTPUT / 'all_nodes.json'}")
    print(f"Saved to {OUTPUT / 'all_edges.json'}")

    # ── Embed all nodes ──
    print(f"\n{'=' * 60}")
    print("Embedding all nodes with BGE Base EN v1.5...")
    from sentence_transformers import SentenceTransformer

    model_path = str(ROOT / "models" / "kg-embeddings" / "models--BAAI--bge-base-en-v1.5" / "snapshots" / "a5beb1e3e68b9ab74eb54cfd186867f64f240e1a")
    model = SentenceTransformer(model_path)

    # Build embedding texts
    texts = []
    for node in all_nodes:
        parts = [node["title"]]
        if node["summary"]:
            parts.append(node["summary"][:300])
        if node["canonical_facts"]:
            parts.append(". ".join(node["canonical_facts"][:3]))
        texts.append(": ".join(parts))

    # Batch embed
    embeddings = model.encode(texts, batch_size=64, show_progress_bar=True, normalize_embeddings=True)
    print(f"Embedded {len(embeddings)} nodes, dim={embeddings.shape[1]}")

    # ── Generate NDJSON for Vectorize ──
    ndjson_path = OUTPUT / "vectors.ndjson"
    with open(ndjson_path, "w") as f:
        for i, node in enumerate(all_nodes):
            record = {
                "id": node["id"],
                "values": embeddings[i].tolist(),
                "metadata": {
                    "subject": node["subject"],
                    "topic": node["topic"],
                    "title": node["title"][:200],
                }
            }
            f.write(json.dumps(record) + "\n")

    print(f"Saved {len(all_nodes)} vectors to {ndjson_path}")
    print(f"File size: {ndjson_path.stat().st_size / 1024 / 1024:.1f} MB")

    print(f"\n{'=' * 60}")
    print("DONE. Next steps:")
    print("  1. Archive old D1 data: wrangler d1 execute prelims-master-db --command 'SELECT * FROM master_nodes' > kg/output/old_master_nodes_backup.sql")
    print("  2. Clear old vectors: wrangler vectorize delete-vectors prelims-concept-vectors --ids ...")
    print("  3. Upsert new vectors: wrangler vectorize upsert prelims-concept-vectors --file kg/output/vectors.ndjson")
    print("  4. Insert nodes into D1: (use the all_nodes.json)")


if __name__ == "__main__":
    main()
