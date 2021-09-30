f_input = open('input.txt', 'r')
f_output = open('output.txt', 'w')
n, m = tuple(map(int, f_input.readline().split()))
cache_dict = dict()
cache_list = []
refuse_dict = dict()
count = 1
for item in range(n):
    mean_record, time_record = tuple(map(str, f_input.readline().split()))
    if mean_record in cache_list:
        if refuse_dict[mean_record] < int(time_record):
            refuse_dict[mean_record] = int(time_record)
            cache_list.append(mean_record)
            cache_list.remove(mean_record)
            f_output.write(f'{count} UPDATE {mean_record}\n')
            count += 1
    else:
        if mean_record in refuse_dict:
            if refuse_dict[mean_record] < int(time_record):
                refuse_dict[mean_record] = int(time_record)
                if len(cache_list) >= m:
                    print(cache_list)
                    f_output.write(f'{count} DELETE {cache_list[0]}\n')
                    cache_list.pop(0)
                cache_list.append(mean_record)
                f_output.write(f'{count} PUT {mean_record}\n')
                count += 1
        else:
            if len(cache_list) >= m:
                f_output.write(f'{count} DELETE {cache_list[0]}\n')
                cache_list.pop(0)
            refuse_dict[mean_record] = int(time_record)
            cache_list.append(mean_record)
            f_output.write(f'{count} PUT {mean_record}\n')
            count += 1
