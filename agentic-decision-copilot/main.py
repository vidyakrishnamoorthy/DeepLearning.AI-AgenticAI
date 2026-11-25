from pprint import pprint
from src.workflow import run


def main():
    print("\nAGENTIC DECISION COPILOT\n")
    decision = input("What decision are you trying to make?\n> ").strip()

    if not decision:
        print("Please enter a decision.")
        return

    result = run(decision)

    print("\n--- PLAN ---")
    pprint(result["plan"])

    print("\n--- INITIAL ANALYSIS ---")
    print(result["draft"])

    print("\n--- CRITIC ---")
    print(result["critique"])

    print("\n--- FINAL RECOMMENDATION ---")
    print(result["final"])

    print("\n--- EVAL ---")
    pprint(result["eval"])


if __name__ == "__main__":
    main()
