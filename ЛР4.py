class Date:

    """Клас для представлення та опрацювання календарної дати (день, місяць, рік).
    Забезпечує перевірку коректності дати, додавання днів, порівняння дат та
       обчислення порядкового номера дня в році."""

    def __init__(self, day: int, month: int, year: int):

        """Ініціалізує об'єкт дата з заданим днем, місяцем і роком.

        Parameters:
            day (int): День місяця (1-31 в залежності від місяця).
            month (int): Місяць (1-12).
            year (int): Рік (має бути додатнім числом).

        Raises:
            TypeError: Якщо будь-який параметр не є цілим числом.
            ValueError: Якщо значення дня або місяця некоректне для вказаного року. """

        if not isinstance(day, int):
            raise TypeError("Помилка! День має бути ціле число!")
        if not isinstance(month, int):
            raise TypeError("Помилка! Місяць має бути ціле число")
        if not isinstance(year, int):
            raise TypeError("Помилка! Рік має бути ціле число")
        if year < 1:
            raise ValueError("Помилка! Рік має бути додатнім!")
        if not month>=1 and month<= 12:
            raise ValueError("Місяців всього 12))))))")
        if not 1 <= day <= self.days_in_month(month, year):
            raise ValueError(f"День {day} неправильний для місяця {month} і року {year}.")
        self._day = day
        self._month = month
        self._year = year

    def __str__(self):

        """Повертає рядкове представлення дати у форматі день.місяць.рік. """

        return f"{self._day}.{self._month}.{self._year}"

    def is_leap_year(self, year: int) -> bool:

        """Перевіряє, чи є вказаний рік високосним.

        Parameters:
            year (int): Рік для перевірки.

        Returns:
            bool: True, якщо рік високосний, інакше False. """

        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(self, month: int, year: int) -> int:

        """ Повертає кількість днів у вказаному місяці заданого року.

        Parameters:
            month (int): Номер місяця (1-12).
            year (int): Рік.

        Returns:
            int: Кількість днів у місяці. """

        if month == 2:
            return 29 if Date.is_leap_year(year) else 28
        if month in [4, 6, 9, 11]:
            return 30
        return 31

    def add_days(self, n: int):

        """ Додає до поточної дати n днів та повертає новий об'єкт Date.

        Parameters:
            n (int): Кількість днів для додавання.

        Returns:
            Date: Нова дата після додавання днів. """

        day = self._day
        month = self._month
        year = self._year

        while n > 0:
            days_in_current_month = self.days_in_month(month, year)
            if day + n <= days_in_current_month:
                day += n
                n = 0
            else:
                n -= (days_in_current_month - day + 1)
                day = 1
                month += 1
                if month > 12:
                    month = 1
                    year += 1
        return Date(day, month, year)

    def __eq__(self, other):

        """ Перевіряє рівність двох дат.

        Parameters:
            other (Date): Інший об'єкт Date для порівняння.

        Returns:
            bool: True, якщо дати однакові, інакше False. """

        if not isinstance(other, Date):
            return False
        return (self._day, self._month, self._year) == (other._day, other._month, other._year)

    def __lt__(self, other):

        """ Перевіряє, чи поточна дата менша за іншу.

        Parameters:
            other (Date): Інший об'єкт Date для порівняння.

        Returns:
            bool: True, якщо поточна дата менша, інакше False. """

        if not isinstance(other, Date):
            return NotImplemented
        return (self._year, self._month, self._day) < (other._year, other._month, other._day)

    def __gt__(self, other):

        """ Перевіряє, чи поточна дата більша за іншу.

        Parameters:
            other (Date): Інший об'єкт Date для порівняння.

        Returns:
            bool: True, якщо поточна дата більша, інакше False. """

        if not isinstance(other, Date):
            return NotImplemented
        return (self._year, self._month, self._day) > (other._year, other._month, other._day)

    def to_ordinal(self) -> int:

        """ Обчислює порядковий номер дня в році для поточної дати.

        Returns:
            int: Порядковий номер дня в році (1–365 або 366). """

        """Повертає порядковий номер дня в році."""

        days_in_months = [31, 29 if self.is_leap_year(self._year) else 28, 31, 30, 31, 30,
                          31, 31, 30, 31, 30, 31]
        return sum(days_in_months[:self._month - 1]) + self._day


if __name__ == "__main__":
    try:
        d1 = Date(30, 4, 2025)
        print("Дата 1:", d1)
        print("Високосний рік?", d1.is_leap_year(d1._year))
        print("Порядковий номер дня в році:", d1.to_ordinal())

        d2 = Date(21, 12, 2023)
        print("Дата 2:", d2)

        print("Чи дата1 = дата2 ?", d1 == d2)
        print("Чи дата1 > дата2 ?", d1 > d2)
        print("Чи дата1 < дата2 ?", d1 < d2)

        d3 = d2.add_days(1)
        print("Дата 2 + 1 день:", d3)

        wrong_date = Date(31, 4, 2025)

        d2 = Date(31, 4, 2023)
    except ValueError as e:
        print(f"Помилка створення дати: {e}")