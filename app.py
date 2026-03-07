

def check_age(age: str) -> int:
    """parbauda vecumu"""
    age = age.strip()
    if not age:
        raise ValueError("gadi nevar but tukši")
    if not age.isdigit():
        raise ValueError("Gadiem jabut ar skaitli")
    age_num = int(age)
    if age_num <= 0:
        raise ValueError("Gadiem jābut vairāk par 0")
    
    return age_num + 1


if __name__ == "__main__":
    age = input("Ievadiet vecumu: ")
    rezultats = check_age(age)
    print(f"Jusu ievaditais vecums ir {rezultats}")