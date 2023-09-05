import csv

from weight.models import Weight

def delete_all_current_weights(user="admin"):
    Weight.objects.filter(user__username=user).delete()

def run():
    with open("/home/victor/python_projects/blog/data/WeightFit_2023-09-02.csv", "r") as f:
        reader_obj = csv.reader(f)

        for row in reader_obj:
            try:
                print(row)
                weight = Weight(created=row[0], mass=row[1])
                weight.save()
            except Exception as e:
                print(e)


delete_all_current_weights()
run()
