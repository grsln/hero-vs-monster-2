## Герой и Чудовища 2: волшебный тотем

#### Шаблоны проектирования

Для реализации выбора типа атаки рыцаря и чудовищ использован шаблон проектирования **Стратегия**. Паттерн выбран в связи с необходимостью изменения поведения в ходе игры.

Шаблон **Посредник** (класс Battle) использован для взаимодействия объектов классов Hero(Рыцарь) и Monster(Чудовище).

Паттерн **Снимок**(классы Game, Snapshot, Totem) применен для сохранения и восстановления игры.
