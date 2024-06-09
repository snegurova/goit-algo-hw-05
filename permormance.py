"""Module providing a performance analyze."""
import timeit

from boyer_moore import boyer_moore
from knuth_morris_pratt import knuth_morris_pratt
from rabin_karp import rabin_karp

# Завантаження текстових файлів
with open("article1.txt", "r") as file:
    text1 = file.read()

with open("article2.txt", "r") as file:
    text2 = file.read()

# Підрядки для пошуку
existing_substring = "структури"
non_existing_substring = "non_existing_substring"

# Вимірювання часу для кожного алгоритму
def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=1000)

bm_time_text1_existing = measure_time(boyer_moore, text1, existing_substring)
kmp_time_text1_existing = measure_time(knuth_morris_pratt, text1, existing_substring)
rk_time_text1_existing = measure_time(rabin_karp, text1, existing_substring)

bm_time_text1_non_existing = measure_time(boyer_moore, text1, non_existing_substring)
kmp_time_text1_non_existing = measure_time(knuth_morris_pratt, text1, non_existing_substring)
rk_time_text1_non_existing = measure_time(rabin_karp, text1, non_existing_substring)

bm_time_text2_existing = measure_time(boyer_moore, text2, existing_substring)
kmp_time_text2_existing = measure_time(knuth_morris_pratt, text2, existing_substring)
rk_time_text2_existing = measure_time(rabin_karp, text2, existing_substring)

bm_time_text2_non_existing = measure_time(boyer_moore, text2, non_existing_substring)
kmp_time_text2_non_existing = measure_time(knuth_morris_pratt, text2, non_existing_substring)
rk_time_text2_non_existing = measure_time(rabin_karp, text2, non_existing_substring)

# Виведення результатів
print(f"Article 1 - Existing Substring:\nBM: {bm_time_text1_existing}, KMP: {kmp_time_text1_existing}, RK: {rk_time_text1_existing}")
print(f"Article 1 - Non-existing Substring:\nBM: {bm_time_text1_non_existing}, KMP: {kmp_time_text1_non_existing}, RK: {rk_time_text1_non_existing}")
print(f"Article 2 - Existing Substring:\nBM: {bm_time_text2_existing}, KMP: {kmp_time_text2_existing}, RK: {rk_time_text2_existing}")
print(f"Article 2 - Non-existing Substring:\nBM: {bm_time_text2_non_existing}, KMP: {kmp_time_text2_non_existing}, RK: {rk_time_text2_non_existing}")