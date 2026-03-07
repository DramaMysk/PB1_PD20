

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
    
    return age_num

def check_name(name: str) -> str:
    """parbauda varbu vai nav tuks, ir ar burtiem"""
    name = name.strip()
    if not name:
        raise ValueError("vards nevar but tuks")
    if not name.isalpha():
        raise ValueError("vardam jabut ar butriem")
    return name


if __name__ == "__main__":
    age = input("Ievadiet vecumu: ")
    name = input("Ieraksti vardu: ")
    rezultats = check_age(age)
    vards = check_name(name)
    print(f"Sveiki, {vards} tev ir {rezultats} gadi ")