# M02 Case Study
# Written by Miguel Rangel using Python 3.11.6 (64-bit); last edit: 11/3/23
# accept student names and GPAs and test if 
# the student qualifies for either the Dean's List or the Honor Roll


def main():
    
    while True:
        
        last_name = input("Enter student's last name or enter 'ZZZ' to quit: ")
        if last_name == 'ZZZ':
            break
        
        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))
        
        if gpa >= 3.5:
            print(first_name, last_name, "has made the Dean's List.")
            
        elif gpa >= 3.25:
            print(first_name, last_name,  "has made the Honor Roll.")
            
        else:
            print(first_name, last_name, "does not qualify for the Dean's List or the Honor Roll.")
            
main()
