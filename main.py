import argparse
import sys
from orchestrator.fraud_orchestrator import FraudOrchestrator


def parse_args():
    parser = argparse.ArgumentParser(
        description="Agentic Fraud Orchestrator",
    )

    # === Business intent ===
    parser.add_argument(
        "--goal",
        required=True,
        choices=["baseline", "ml_train", "serve", "deploy", "monitor", "heal"],
        help="High-level intent to execute"
    )

    parser.add_argument(
        "--name",
        required=True,
        help="Logical dataset / project name"
    )

    parser.add_argument(
        "--dataset-path",
        required=True,
        help="Path or URI to dataset"
    )

    parser.add_argument(
        "--prefix",
        default="init",
        choices=["init", "replay", "hotfix", "shadow", "prod"],
        help="Artifact lifecycle prefix"
    )

    parser.add_argument(
        "--mode",
        choices=["local", "cloud", "localstack"],
        default="local",
        help="Execution & storage mode"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    # dataset_path "data/data.csv"

    orchestrator = FraudOrchestrator(
        intent=args.goal,
        project=args.name,
        dataset_path=args.dataset_path,
        prefix=args.prefix,
        mode=args.mode,   # config, storage
    )

    result = orchestrator.run()
    
    if result["success"]:
        print(f"Execution completed: {result['summary']}")
    else:
        print(f"Execution failed: {result['error']}")
        exit(1)


if __name__ == "__main__":
    main()

"""
Examples:
  python main.py --goal baseline --name fraud-dev --dataset-path ./data/wine.csv --mode local
  python main.py --goal ml_train --name fraud --dataset-path s3://bucket/data.csv --mode cloud
  python main.py --goal deploy --name fraud-simulate --dataset-path ./data/fraud.csv --mode localstack
"""