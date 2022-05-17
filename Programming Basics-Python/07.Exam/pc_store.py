dollar = 1.57
processor_in_usd = float(input())
gpu_in_usd = float(input())
ram_in_usd = float(input())
number_of_ram = int(input())
discount_percent = float(input())

processor_in_bgn = processor_in_usd * dollar
gpu_in_bgn = gpu_in_usd * dollar
ram_in_bgn = ram_in_usd * dollar
ram_total = ram_in_bgn * number_of_ram
processor_in_bgn_total = processor_in_bgn - (processor_in_bgn * discount_percent)
gpu_in_bgn_total = gpu_in_bgn - (gpu_in_bgn * discount_percent)
total_sum = ram_total + processor_in_bgn_total + gpu_in_bgn_total
print(f'Money needed - {total_sum:.2f} leva.')