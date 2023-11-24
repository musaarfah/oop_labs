def is_valid_rollno(roll_no):
    if roll_no[0]!='B':
        return False
    return True
    
def is_valid_score(score):
    if score=='AB'or score== '':
        return False
    return True

def is_valid_course(course):
    if course=='ITC' or course=='PF' or course=='DLD':
        return True
    return False

def is_valid_record(record):
    fields = record.split()
    if len(fields)!=6:
        return False
    

    if not is_valid_rollno(fields[0]):
        return False

    for score in fields[3:]:
        if not is_valid_score(score):
            return False
        

    return True



def validate_records(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        errors_count = 0
        line_number = 0

        for line in input_file:
            line_number += 1
            if line_number <= 2:
                continue

            if not is_valid_record(line):
                errors_count += 1
                output_file.write(f"Error in record {line_number}:\n")
                output_file.write(line)
        print(f"Total number of errored lines: {errors_count}")



input_filename = 'grades.txt'
output_filename = 'error_output.txt'
validate_records(input_filename, output_filename)
    