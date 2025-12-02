with open('input.txt') as f:
    product_ids = f.read().split(',')

invalid_product_ids = []
invalid_product_ids_part2 = []

for product_id_range in product_ids:
    start, end = map(int, product_id_range.split('-'))
    for product_id in range(start, end + 1):
        product_id = str(product_id)
        length = len(product_id)
        mid = length // 2
        if product_id[:mid] == product_id[mid:] and length % 2 == 0:
            invalid_product_ids.append(int(product_id))
            invalid_product_ids_part2.append(int(product_id))
            continue
        for i in range(1, mid + 1):
            multiple = length  / i
            if not multiple.is_integer():
                continue
            if product_id == (product_id[:i] * int(multiple)):
                invalid_product_ids_part2.append(int(product_id))
                break

print('part 1', sum(invalid_product_ids));
print('part 2', sum(invalid_product_ids_part2));
