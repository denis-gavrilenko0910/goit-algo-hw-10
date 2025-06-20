import pulp


def optimize_production():
    """
    Solves a linear programming problem to maximize the total production of Lemonade and Fruit Juice
    given resource constraints using the PuLP library. Prints the optimal production quantities.
    """
    # Создание задачи
    problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

    # Определение переменных
    lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
    fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

    # Ограничения ресурсов
    problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
    problem += 1 * lemonade <= 50, "Sugar_Constraint"
    problem += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
    problem += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

    # Целевая функция (максимизация производства)
    problem += lemonade + fruit_juice, "Total_Production"

    # Решение задачи
    problem.solve()

    # Вывод результатов
    print(f"Status: {pulp.LpStatus[problem.status]}")
    print(f"Lemonade produced: {lemonade.varValue}")
    print(f"Fruit Juice produced: {fruit_juice.varValue}")
    print(f"Total Production: {pulp.value(problem.objective)}")

if __name__ == "__main__":
    optimize_production()
