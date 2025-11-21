from typing import Any


def ask_choice(prompt: str, choices: dict[str, str]) -> str:
    print(prompt)
    for key, text in choices.items():
        print(f"{key}. {text}")
    while True:
        ans = input("Введи номер варианта: ").strip()
        if ans in choices:
            return ans
        print("Некорректный выбор, попробуй ещё раз.")

def collect_facts() -> dict[str, Any]:
    goal_map = {
        "1": ("own_use", "Покупка для собственного проживания"),
        "2": ("investment", "Инвестиция под аренду"),
        "3": ("speculation", "Краткосрочная спекуляция (перепродажа)"),
    }
    goal_choice = ask_choice(
        "Какова твоя основная цель на рынке недвижимости?",
        {k: v[1] for k, v in goal_map.items()},
    )
    goal_code = goal_map[goal_choice][0]

    price_trend_map = {
        "1": ("strong_growth", "Цены сильно растут"),
        "2": ("moderate_growth", "Цены умеренно растут"),
        "3": ("stable", "Цены в целом стабильны"),
        "4": ("decline", "Цены снижаются"),
    }
    price_trend_choice = ask_choice(
        "Как ты оцениваешь динамику цен на жилье в регионе?",
        {k: v[1] for k, v in price_trend_map.items()},
    )
    price_trend_code = price_trend_map[price_trend_choice][0]

    rental_yield_map = {
        "1": ("low", "Низкая (аренда дешевая относительно цены)"),
        "2": ("medium", "Средняя"),
        "3": ("high", "Высокая (аренда дорогая относительно цены)"),
    }
    rental_yield_choice = ask_choice(
        "Как ты оцениваешь доходность аренды (соотношение аренды к цене)?",
        {k: v[1] for k, v in rental_yield_map.items()},
    )
    rental_yield_code = rental_yield_map[rental_yield_choice][0]

    liquidity_map = {
        "1": ("fast", "Объекты продаются быстро (недели)"),
        "2": ("medium", "Объекты продаются в среднем (1–3 месяца)"),
        "3": ("slow", "Объекты продаются долго (полгода и более)"),
    }
    liquidity_choice = ask_choice(
        "Какова, по твоим наблюдениям, скорость продажи типичных объектов?",
        {k: v[1] for k, v in liquidity_map.items()},
    )
    liquidity_code = liquidity_map[liquidity_choice][0]

    mortgage_rate_map = {
        "1": ("low", "Низкие"),
        "2": ("medium", "Средние"),
        "3": ("high", "Высокие"),
    }
    mortgage_choice = ask_choice(
        "Как ты оцениваешь текущий уровень ипотечных ставок?",
        {k: v[1] for k, v in mortgage_rate_map.items()},
    )
    mortgage_code = mortgage_rate_map[mortgage_choice][0]

    horizon_map = {
        "1": ("short", "До 3 лет"),
        "2": ("medium", "3–7 лет"),
        "3": ("long", "Больше 7 лет"),
    }
    horizon_choice = ask_choice(
        "Каков твой горизонт планирования владения недвижимостью?",
        {k: v[1] for k, v in horizon_map.items()},
    )
    horizon_code = horizon_map[horizon_choice][0]

    risk_profile_map = {
        "1": ("low", "Низкий (избегаешь рисков)"),
        "2": ("medium", "Умеренный"),
        "3": ("high", "Высокий (готов к риску ради доходности)"),
    }
    risk_choice = ask_choice(
        "Как бы ты оценил свою готовность к финансовому риску?",
        {k: v[1] for k, v in risk_profile_map.items()},
    )
    risk_profile_code = risk_profile_map[risk_choice][0]

    facts = {
        "goal": goal_code,
        "price_trend": price_trend_code,
        "rental_yield": rental_yield_code,
        "liquidity": liquidity_code,
        "mortgage_rate": mortgage_code,
        "horizon": horizon_code,
        "risk_profile": risk_profile_code,
    }

    return facts
