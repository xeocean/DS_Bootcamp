from analytics import Research
from config import *

if __name__ == "__main__":
    research = None
    try:
        research = Research()
        research.set_attributes(file_path)
        if research.my_list is not None:
            zero, one = research.calc.counts(research.my_list)
            zero_percent, one_percent = research.calc.fractions(zero, one)
            new_result = research.analytics.predict_random(count_random)
            zero_new, one_new = research.calc.counts(new_result)
            text = template.format(zero + one, zero, one, round(zero_percent, 2), round(one_percent, 2),
                                   count_random, zero_new, one_new)
            research.save_file(text, file_output)
            research.send_message(status=True)
        else:
            research.send_message(status=False)
    except ValueError as e:
        if research is not None:
            research.send_message(status=False)
        print(f'Error: {e}')
