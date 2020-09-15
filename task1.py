from sys import argv

scrypt_name, working_hours, rate_hour, prize = argv

print(f"Заработная плата сотрудника = {float(working_hours) * float(rate_hour) + float(prize)}")
