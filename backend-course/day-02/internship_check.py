python_level = int(input("Знание Python от 1 до 10: "))
sql_level = int(input("Знание SQL от 1 до 10: "))
git_level = int(input("Знание Git от 1 до 10: "))

if python_level >= 6 and sql_level >= 4 and git_level >= 4:
    print("Можно отправлять резюме на стажировку")
elif python_level>=4:
    print("База есть, но стоит повторить SQL и Git")
else:
    print("Рекомендуется улучшить навыки перед отправкой резюме на стажировку")