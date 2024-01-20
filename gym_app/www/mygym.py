
import frappe

def get_context(context):
    # workout_plans=frappe.get_all('Gym Workout Plan',filters={"published": 1}, fields=['plan_name', 'difficulty_level', 'description', 'allocated_trainer'],as_list=True)
    # for workout_plan in workout_plans:
    #     # Fetch the full WorkoutPlan document
    #     workout_plan_doc = frappe.get_doc('Gym Workout Plan', workout_plan[0])
        
    #     # Access the 'exercises' field in the WorkoutPlan document, which is a list representing the child table
    #     exercises = workout_plan_doc.get('Gym Workout Plan Exercise')

    #     workout_plan['exercises'] = exercises
    # context.plans = workout_plans

    # parent_doctype = 'Gym Workout Plan'
    # child_doctype = 'Gym Workout Plan Exercise'

    # # Define the fields to fetch from both parent and child tables
    # fields = [
    #     f'{parent_doctype}.name',
    #     f'{parent_doctype}.plan_name',
    #     f'{parent_doctype}.difficulty_level',
    #     f'{parent_doctype}.description',
    #     f'{parent_doctype}.published',
    #     f'{parent_doctype}.allocated_trainer',
    #     f'{child_doctype}.exercise_name',
    #     f'{child_doctype}.sets',
    #     f'{child_doctype}.repetitions',
    #     f'{child_doctype}.rest_time'
    # ]

    # # Define the join condition
    # join_condition = f'{parent_doctype}.name = {child_doctype}.parent'

    # # Fetch data using frappe.get_all with join
    # data = frappe.get_all(
    #     parent_doctype,
    #     fields=fields,
    #     filters={},
    #     join={child_doctype: join_condition},
    #     as_list=True
    # )

    # # Organize data into a nested structure
    # workout_plans = {}
    # for row in data:
    #     (
    #         parent_name, plan_name, difficulty_level, description,
    #         published, allocated_trainer, exercise_name, sets, repetitions, rest_time
    #     ) = row
    #     if parent_name not in workout_plans:
    #         workout_plans[parent_name] = {
    #             'name': parent_name,
    #             'plan_name': plan_name,
    #             'difficulty_level': difficulty_level,
    #             'description': description,
    #             'published': published,
    #             'allocated_trainer': allocated_trainer,
    #             'exercises': []
    #         }
    #     exercise = {
    #         'exercise_name': exercise_name,
    #         'sets': sets,
    #         'repetitions': repetitions,
    #         'rest_time': rest_time
    #     }
    #     workout_plans[parent_name]['exercises'].append(exercise)

    # # Pass the data to the context
    # context['workout_plans'] = list(workout_plans.values())
    context.plans = frappe.get_all('Gym Workout Plan', 
        fields=['name' , 'plan_name', 'difficulty_level', 'description', 'published', 'allocated_trainer'],
        filters={'published': 1},
        join={
            'Gym Workout Plan Exercise': {
                'fields': ['exercise_name', 'sets', 'repetitions', 'rest_time'],
                'on': 'Gym Workout Plan.name = Gym Workout Plan Exercise.parent'
            }
        }
    )
    return context