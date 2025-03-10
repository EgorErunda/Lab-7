import requests

def get_vacancies(search_text, area=None, per_page=10):
    url = "https://api.hh.ru/vacancies"

    params = {
        'text': search_text,  
        'area': area,         
        'per_page': per_page, 
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('items', [])  
    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
        return []

def print_vacancies(vacancies):
    """
    Функция для вывода информации о вакансиях.
    :param vacancies: Список вакансий.
    """
    for vacancy in vacancies:
        print(f"Вакансия: {vacancy['name']}")
        print(f"Компания: {vacancy['employer']['name']}")
        salary = vacancy.get('salary')
        if salary:
            salary_from = salary.get('from', 'Не указано')
            salary_to = salary.get('to', 'Не указано')
            currency = salary.get('currency', '')
            print(f"Зарплата: от {salary_from} до {salary_to} {currency}")
        else:
            print("Зарплата: Не указана")
        print(f"Ссылка: {vacancy['alternate_url']}")
        experience = vacancy.get('experience', {}).get('name', 'Не указан')
        print(f"Требуемый опыт работы: {experience}")
        
        print("-" * 50)

if __name__ == "__main__":
    search_text = "Python разработчик"  
    area = 1  # Регион (1 — Москва, 2-СПБ и тд)
    per_page = 6  #(кол-во вакансий)
    vacancies = get_vacancies(search_text, area, per_page)
    if vacancies:
        print(f"Найдено вакансий: {len(vacancies)}")
        print_vacancies(vacancies)
    else:
        print("Вакансии не найдены.")