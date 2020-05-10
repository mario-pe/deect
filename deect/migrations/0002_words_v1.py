from django.db import migrations

WORDS = [
    {"word":"cat","translation": "pies", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"dog","translation": "kot", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"partlly","translation": "częśćiowo", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"partly","translation": "częśćiowo", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"oven","translation": "piekarnik", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"faulty","translation": "wadliwy", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"tamper","translation":"majstrować", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"footage","translation":"filmik", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"tamper with footage","translation":"majstrować przy filmie", "tutor":"Luk", "date":"2019-04-15", "category": "sentence"},
    {"word":"tampered footage","translation":"z majstrowany film", "tutor":"Luk", "date":"2019-04-15", "category": "sentence"},
    {"word":"settle","translation":"roztrzygać", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"come to terms","translation":"roztrzygać", "tutor":"Luk", "date":"2019-04-15", "category": "sentence"},
    {"word":"snitch","translation":"kapuś", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"siblings","translation":"rodzeństwo", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"accuse","translation":"oskarzac", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"bearable","translation":"znośny", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"I can't stand","translation":"Nie mogę wytrzymać", "tutor":"Luk", "date":"2019-04-15", "category": "sentence"},
    {"word":"I can't stand this person","translation":"Nie moge wytrzymać tej osoby",  "tutor":"Luk", "date":"2019-04-15", "category": "sentence"},
    {"word":"cramps","translation":"skurcze", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"baffled","translation":"zaskoczony", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"frenzy","translation":"szał", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"social circle","translation":"krąg znajomych", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"bound to","translation":"cos sie musi zdarzyć", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"crust","translation":"spód od pizzy", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"dough","translation":"", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"pastry","translation":"rogalik", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"anticipate","translation":"oczekiwać", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"edible","translation":"jadalny", "tutor":"Luk", "date":"2019-04-15", "category": "word"},
    {"word":"Poland got of the hook from an economical crash","translation":"Polska wybrneła z kryzysu economicznego", "tutor":"Luk", "date":"2019-08-04", "category": "sentence"},
    {"word":"got of the hook","translation":"wybrnąć z kłopotliwej sytuacji", "tutor":"Luk", "date":"2019-08-04", "category": "sentence"},
    {"word":"on the money","translation":"wygrałes, masz racje", "tutor":"Luk", "date":"2019-08-04", "category": "sentence"},
    {"word":"on the ball","translation":"robić dobrą robote", "tutor":"Luk", "date":"2019-08-04", "category": "sentence"},
    {"word":"hit the sack","translation":"położyć sie spać", "tutor":"Luk", "date":"2019-08-04", "category": "sentence"},
    {"word":"collar bone","translation":"obojczyk", "tutor":"Luk", "date":"2019-08-04", "category": "word"},
    {"word":"cast","translation":"gips", "tutor":"Luk", "date":"2019-08-04", "category": "word"},
    {"word":"frigle","translation":"kruchy", "tutor":"Luk", "date":"2019-08-04", "category": "word"},
    {"word":"finely","translation":"drobno", "tutor":"Luk", "date":"2019-08-04", "category": "word"},
    {"word":"robust","translation":"solidny", "tutor":"Luk", "date":"2019-08-04", "category": "word"},
    {"word":"chop","translation":"siekać", "tutor":"Luk", "date":"2019-08-04", "category": "word"},
    {"word":"dice","translation":"siekać", "tutor":"Luk", "date":"2019-08-04", "category": "word"},
    {"word":"slice","translation":"siekać", "tutor":"Luk", "date":"2019-08-04", "category": "word"},
    {"word":"medicore","translation":"średni", "tutor":"Luk", "date":"2019-08-04", "category": "word"},
    {"word":"staple","translation":"podstawowy", "tutor":"Luk", "date":"2019-08-04", "category": "word"},
    {"word":"it was a staple my diet","translation":"to była podstawa mojej diety ", "tutor":"Luk", "date":"2019-08-04", "category": "sentence"},
    {"word":"candy bar","translation":"baton", "tutor":"Luk", "date":"2019-08-04", "category": "word"},
    {"word":"whip somethin up","translation":"podsycać coś(złość)", "tutor":"Luk", "date":"2019-08-04", "category": "sentence"},
    {"word":"whip out" ,"translation":"wziąć cos szybko", "tutor":"Luk", "date":"2019-08-04", "category": "sentence"},
    {"word":"grate potatos","translation":"obierać ziemniaki", "tutor":"Luk", "date":"2019-08-04", "category": "word"},
    {"word":"fickle","translation":"kapryśny", "tutor":"Luk", "date":"2019-08-04", "category": "word"},
    {"word":"picky","translation":"kapryśny", "tutor":"Luk", "date":"2019-08-04", "category": "word"},
]

def forwards_func(apps, schema_editor):
    Words = apps.get_model("deect", "Word")
    db_alias = schema_editor.connection.alias
    Words.objects.using(db_alias).bulk_create(
        [Words(**x) for x in WORDS]
    )


def reverse_func(apps, schema_editor):
    Words = apps.get_model("deect", "Word")
    db_alias = schema_editor.connection.alias
    for group_parameter in WORDS:
        Words.objects.using(db_alias).filter(
            **group_parameter
        ).delete()


class Migration(migrations.Migration):

    dependencies = [("deect", "0001_initial")]

    operations = [migrations.RunPython(forwards_func, reverse_func)]
