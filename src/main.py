from builder import build_knowledge_base
from interface import collect_facts



def main() -> None:
    print("Экспертная система для анализа рынка недвижимости")
    print("-" * 70)

    kb = build_knowledge_base()
    facts = collect_facts()
    fired_rules = kb.infer(facts)

    print("\nРезультаты анализа:\n")

    if not fired_rules:
        print("По введённым данным система не смогла сформировать явные рекомендации.")
        print("Рекомендуется дополнительно обратиться к профильным аналитическим материалам.")
    else:
        for i, rule in enumerate(fired_rules, start=1):
            print(f"{i}. {rule.description}")
            print(rule.recommendation)
            print()

    print("Работа экспертной системы завершена.")


if __name__ == "__main__":
    main()