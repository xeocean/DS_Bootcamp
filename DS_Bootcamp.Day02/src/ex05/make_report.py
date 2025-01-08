from analytics import Research
from config import *

if __name__ == "__main__":
    try:
        research = Research(file_path)
        for_print = research.file_reader()
        if for_print is not None:
            zero, one = research.calc.counts(for_print)
            zero_percent, one_percent = research.calc.fractions(zero, one)
            new_result = research.analytics.predict_random(count_random)
            zero_new, one_new = research.calc.counts(new_result)
            text = template.format(zero + one, zero, one, round(zero_percent, 2), round(one_percent, 2),
                                   count_random, zero_new, one_new)
            research.save_file(text, file_output)
    except ValueError as e:
        print(f'Error: {e}')
