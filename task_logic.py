if __name__ == '__main__':
    import libneuro
    nn = libneuro.NeuroNetLibrary()
    nlu = libneuro.NeuroNluLibrary()
    nv = libneuro.NeuroVoiceLibrary()
    InvalidCallStateError = libneuro.InvalidCallStateError
    check_call_state = libneuro.check_call_state


    def main():
        nn.call(nn.dialog['msisdn'], '2020-05-20 14:20:00', entry_point='main_online')


    def main_online():
        pass


# hello_unit

@check_call_state(nv)
def hello_main_play_and_detect():
    nv.set_default('listen', {'no_input_timeout': 6000, 'recognition_timeout': 60000, 'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000})
    with nv.listen(500, entities=[
        'payment_problem',
        'internet_problem',
        'tv_problem',
        'repeat',
        'robot',
        'operator'
    ]) as r:
        pass
    return hello_logic(r)


@check_call_state(nv)
def hello_main():
    nn.log('unit', 'hello_unit')
    nv.say('hello_main_prompt')
    return hello_main_play_and_detect()


@check_call_state(nv)
def hello_default():
    nn.log('unit', 'hello_main')
    nv.say('hello_default_prompt')
    return hello_main_play_and_detect()


@check_call_state(nv)
def hello_null():
    if nn.counter('hello_null', '+') > 1:
        attempt = nn.env('attempt')
        return goodbye_null()
    nn.log('unit', 'hello_unit')
    nv.say('hello_null_prompt')
    return hello_main_play_and_detect()


@check_call_state(nv)
def hello_repeat():
    nn.log('unit', 'hello_main')
    nv.say('hello_repeat_prompt')
    return hello_main_play_and_detect()


@check_call_state(nv)
def hello_robot():
    nn.log('unit', 'hello_main')
    nv.say('hello_robot_prompt')
    return hello_main_play_and_detect()

# //--//--//--//--//--//--//


# payment_unit

@check_call_state(nv)
def payment_play_and_detect():
    nv.set_default('listen', {'no_input_timeout': 6000, 'recognition_timeout': 60000, 'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000})
    with nv.listen(500, entities=[
        'pay_site',
        'offices',
        'repeat',
        'promise_pay',
        'operator',
        'confirm'
    ]) as r:
        pass
    return payment_logic(r)


@check_call_state(nv)
def payment_main():
    nn.log('unit', 'payment_main')
    nv.say('payment_main_prompt')
    return payment_play_and_detect()


@check_call_state(nv)
def payment_default():
    nn.log('unit', 'payment_unit')
    nv.say('payment_default_prompt')
    return payment_play_and_detect()


@check_call_state(nv)
def payment_site():
    nn.log('unit', 'payment_unit')
    nv.say('payment_site_prompt')
    return payment_play_and_detect()


@check_call_state(nv)
def payment_offices():
    nn.log('unit', 'payment_unit')
    nv.say('payment_offices_prompt')
    return payment_play_and_detect()


@check_call_state(nv)
def payment_repeat():
    nn.log('unit', 'payment_unit')
    nv.say('payment_repeat_prompt')
    return payment_play_and_detect()


@check_call_state(nv)
def payment_null():
    if nn.counter('payment_null', '+') > 1:
        attempt = nn.env('attempt')
        return goodbye_null()
    nn.log('unit', 'payment_unit')
    nv.say('payment_null_prompt')
    return payment_play_and_detect()


@check_call_state(nv)
def payment_promise_pay():
    nn.log('unit', 'payment_unit')
    nv.say('payment_promise_pay_prompt')
    return payment_play_and_detect()

# //--//--//--//--//--//--//


# tv_unit

@check_call_state(nv)
def tv_play_and_detect():
    nv.set_default('listen', {'no_input_timeout': 6000, 'recognition_timeout': 60000, 'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000})
    with nv.listen(500, entities=[
        'repeat',
        'robot',
        'confirm',
        'operator'
    ]) as r:
        pass
    return tv_logic(r)


@check_call_state(nv)
def tv_main():
    nn.log('unit', 'tv_main')
    nv.say('tv_main_prompt')
    return tv_play_and_detect()


@check_call_state(nv)
def tv_default():
    nn.log('unit', 'tv_unit')
    nv.say('tv_default_prompt')
    return tv_play_and_detect()


@check_call_state(nv)
def tv_null():
    if nn.counter('tv_null', '+') > 1:
        attempt = nn.env('attempt')
        return goodbye_null()
    nn.log('unit', 'tv_unit')
    nv.say('tv_null_prompt')
    return tv_play_and_detect()


@check_call_state(nv)
def tv_repeat():
    nn.log('unit', 'tv_unit')
    nv.say('tv_repeat_prompt')
    return tv_play_and_detect()


@check_call_state(nv)
def tv_robot():
    nn.log('unit', 'tv_unit')
    nv.say('tv_robot_prompt')
    return tv_play_and_detect()

# //--//--//--//--//--//--//


# internet_unit

@check_call_state(nv)
def internet_play_and_detect():
    nv.set_default('listen', {'no_input_timeout': 6000, 'recognition_timeout': 60000, 'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000})
    with nv.listen(500, entities=[
        'robot',
        'repeat',
        'operator',
        'confirm'
    ]) as r:
        pass
    return internet_logic(r)


@check_call_state(nv)
def internet_main():
    nn.log('unit', 'internet_main')
    nv.say('internet_main_prompt')
    return internet_play_and_detect()


@check_call_state(nv)
def internet_default():
    nn.log('unit', 'internet_unit')
    nv.say('internet_default_prompt')
    return internet_play_and_detect()


@check_call_state(nv)
def internet_null():
    if nn.counter('internet_null', '+') > 1:
        attempt = nn.env('attempt')
        return goodbye_null()
    nn.log('unit', 'internet_unit')
    nv.say('internet_null_prompt')
    return internet_play_and_detect()


@check_call_state(nv)
def internet_robot():
    nn.log('unit', 'internet_unit')
    nv.say('internet_robot_prompt')
    return internet_play_and_detect()


@check_call_state(nv)
def internet_repeat():
    nn.log('unit', 'internet_unit')
    nv.say('internet_repeat_prompt')
    return internet_play_and_detect()

# //--//--//--//--//--//--//


# internet_green_unit

@check_call_state(nv)
def internet_green_play_and_detect():
    nv.set_default('listen', {'no_input_timeout': 6000, 'recognition_timeout': 60000, 'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000})
    with nv.listen(500, entities=[
        'confirm',
        'operator',
        'repeat',
        'robot'
    ]) as r:
        pass
    return internet_green_logic(r)


@check_call_state(nv)
def internet_green_main():
    nn.log('unit', 'internet_green_main')
    nv.say('internet_green_main_prompt')
    return internet_green_play_and_detect()


@check_call_state(nv)
def internet_green_default():
    nn.log('unit', 'internet_green_unit')
    nv.say('internet_green_default_prompt')
    return internet_green_play_and_detect()


@check_call_state(nv)
def internet_green_null():
    if nn.counter('internet_green_null', '+') > 1:
        attempt = nn.env('attempt')
        return goodbye_null()
    nn.log('unit', 'internet_green_unit')
    nv.say('internet_green_null_prompt')
    return internet_green_play_and_detect()


@check_call_state(nv)
def internet_green_repeat():
    nn.log('unit', 'internet_green_unit')
    nv.say('internet_green_repeat_prompt')
    return internet_green_play_and_detect()


@check_call_state(nv)
def internet_green_robot():
    nn.log('unit', 'internet_green_unit')
    nv.say('internet_green_robot_prompt')
    return internet_green_play_and_detect()

# //--//--//--//--//--//--//


# more_question_unit

@check_call_state(nv)
def more_question_play_and_detect():
    nv.set_default('listen', {'no_input_timeout': 6000, 'recognition_timeout': 60000, 'speech_complete_timeout': 2500,
                              'asr_complete_timeout': 6000})
    with nv.listen(500, entities=[
        'payment_problem',
        'internet_problem',
        'tv_problem',
        'robot',
        'no_question',
        'operator',
        'confirm'
    ]) as r:
        pass
    return more_question_logic(r)


@check_call_state(nv)
def more_question_main():
    nn.log('unit', 'more_question_main')
    nv.say('more_question_main_prompt')
    return more_question_play_and_detect()


@check_call_state(nv)
def more_question_default():
    nn.log('unit', 'more_question_unit')
    nv.say('more_question_default_prompt')
    return more_question_play_and_detect()


@check_call_state(nv)
def more_question_null():
    if nn.counter('more_question_null', '+') > 1:
        attempt = nn.env('attempt')
        return goodbye_null()
    nn.log('unit', 'more_question_unit')
    nv.say('more_question_null_prompt')
    return more_question_play_and_detect()


@check_call_state(nv)
def more_question_robot():
    nn.log('unit', 'more_question_unit')
    nv.say('more_question_robot_prompt')
    return more_question_play_and_detect()


@check_call_state(nv)
def more_question_confirm():
    nn.log('unit', 'more_question_unit')
    nv.say('more_question_confirm_prompt')
    return more_question_play_and_detect()

# //--//--//--//--//--//--//


# goodbye_unit

def goodbye_main():
    nn.log('unit', 'goodbye_main')
    nv.say('goodbye_main_prompt')
    nv.hangup()
    return


def goodbye_null():
    nn.log('unit', 'goodbye_main')
    nv.say('goodbye_null_prompt')
    nv.hangup()
    return


def goodbye_operator():
    nn.log('unit', 'goodbye_main')
    nv.say('goodbye_operator_prompt')
    nv.hangup()
    return


def goodbye_operator_demand():
    nn.log('unit', 'goodbye_main')
    nv.say('goodbye_operator_demand_prompt')
    nv.hangup()
    return


def goodbye_internet_green():
    nn.log('unit', 'goodbye_main')
    nv.say('goodbye_internet_green_prompt')
    nv.hangup()
    return

# //--//--//--//--//--//--//

# Логика условий для hello_unit

@check_call_state(nv)
def hello_logic(r):
    """Функция проверки сущностей """
    nn.log('unit', 'hello_unit')
    hello_unit_exec_count = nn.env('hello_unit_exec_count')
    if not hello_unit_exec_count:
        nn.env('hello_unit_exec_count', 1)
    else:
        hello_unit_exec_count = hello_unit_exec_count + 1
        nn.env('hello_unit_exec_count', hello_unit_exec_count)
        if hello_unit_exec_count and hello_unit_exec_count > 10:
            nn.log("Recursive execution detected")
            return

    if not r:
        nn.log("condition", "NULL")
        return hello_null()

    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        return hello_default()

    if r.has_entity("repeat"):
        if r.entity("repeat") == 'true':
            nn.log("condition", "repeat=True")
            return hello_repeat()

    if r.has_entity("payment_problem"):
        if r.entity("payment_problem") == 'true':
            nn.log("condition", "payment_problem=True")
            return payment_main()

    if r.has_entity("internet_problem"):
        if r.entity("internet_problem") == 'true':
            nn.log("condition", "internet_problem=True")
            return internet_main()

    if r.has_entity("tv_problem"):
        if r.entity("tv_problem") == 'true':
            nn.log("condition", "tv_problem=True")
            return tv_main()

    if r.has_entity("robot"):
        if r.entity("robot") == 'true':
            nn.log("condition", "robot=True")
            return hello_robot()

    if r.has_entity("operator"):
        if r.entity("operator") == 'true':
            nn.log("condition", "operator=True")
            return goodbye_operator_demand()

    return hello_default()

# //--//--//--//--//--//--//

# Логика условий для payment_unit

@check_call_state(nv)
def payment_logic(r):
    nn.log('unit', 'payment_unit')
    payment_unit_exec_count = nn.env('payment_unit_exec_count')
    if not payment_unit_exec_count:
        nn.env('payment_unit_exec_count', 1)
    else:
        payment_unit_exec_count = payment_unit_exec_count + 1
        nn.env('payment_unit_exec_count', payment_unit_exec_count)
        if payment_unit_exec_count and payment_unit_exec_count > 10:
            nn.log("Recursive execution detected")
            return

    if not r:
        nn.log("condition", "NULL")
        return payment_null()

    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        return payment_default()

    if r.has_entity("repeat"):
        if r.entity("repeat") == 'true':
            nn.log("condition", "repeat=True")
            return payment_repeat()

    if r.has_entity("operator"):
        if r.entity("operator") == 'true':
            nn.log("condition", "operator=True")
            return goodbye_operator_demand()

    if r.has_entity("pay_site"):
        if r.entity("pay_site") == 'true':
            nn.log("condition", "pay_site=True")
            return payment_site()

    if r.has_entity("offices"):
        if r.entity("offices") == 'true':
            nn.log("condition", "offices=True")
            return payment_offices()

    if r.has_entity("promise_pay"):
        if r.entity("promise_pay") == 'true':
            nn.log("condition", "promise_pay=True")
            return payment_promise_pay()

    if r.has_entity("confirm"):
        if r.entity("confirm") == 'true':
            nn.log("condition", "confirm=True")
            return more_question_main()
        if r.entity("confirm") == 'false':
            nn.log("condition", "confirm=False")
            return goodbye_main()

    return payment_default()

# //--//--//--//--//--//--//

# Логика условий для tv_unit

@check_call_state(nv)
def tv_logic(r):
    nn.log('unit', 'tv_unit')
    tv_unit_exec_count = nn.env('tv_unit_exec_count')
    if not tv_unit_exec_count:
        nn.env('tv_unit_exec_count', 1)
    else:
        tv_unit_exec_count = tv_unit_exec_count + 1
        nn.env('tv_unit_exec_count', tv_unit_exec_count)
        if tv_unit_exec_count and tv_unit_exec_count > 10:
            nn.log("Recursive execution detected")
            return

    if not r:
        nn.log("condition", "NULL")
        return tv_null()

    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        return tv_default()

    if r.has_entity("repeat"):
        if r.entity("repeat") == 'true':
            nn.log("condition", "repeat=True")
            return tv_repeat()

    if r.has_entity("robot"):
        if r.entity("robot") == 'true':
            nn.log("condition", "robot=True")
            return tv_robot()

    if r.has_entity("operator"):
        if r.entity("operator") == 'true':
            nn.log("condition", "operator=True")
            return goodbye_operator_demand()

    if r.has_entity("confirm"):
        if r.entity("confirm") == 'true':
            nn.log("condition", "confirm=True")
            return more_question_main()
        if r.entity("confirm") == 'false':
            nn.log("condition", "confirm=False")
            return goodbye_main()

    return tv_default()

# //--//--//--//--//--//--//

# Логика условий для internet_unit

@check_call_state(nv)
def internet_logic(r):
    nn.log('unit', 'internet_unit')
    internet_unit_exec_count = nn.env('internet_unit_exec_count')
    if not internet_unit_exec_count:
        nn.env('internet_unit_exec_count', 1)
    else:
        internet_unit_exec_count = internet_unit_exec_count + 1
        nn.env('internet_unit_exec_count', internet_unit_exec_count)
        if internet_unit_exec_count and internet_unit_exec_count > 10:
            nn.log("Recursive execution detected")
            return

    if not r:
        nn.log("condition", "NULL")
        return internet_null()

    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        return internet_default()

    if r.has_entity("repeat"):
        if r.entity("repeat") == 'true':
            nn.log("condition", "repeat=True")
            return internet_repeat()

    if r.has_entity("robot"):
        if r.entity("robot") == 'true':
            nn.log("condition", "robot=True")
            return internet_robot()

    if r.has_entity("operator"):
        if r.entity("operator") == 'true':
            nn.log("condition", "operator=True")
            return goodbye_operator_demand()

    if r.has_entity("confirm"):
        if r.entity("confirm") == 'true':
            nn.log("condition", "confirm=True")
            return goodbye_operator()
        if r.entity("confirm") == 'false':
            nn.log("condition", "confirm=False")
            return internet_green_main()

    return internet_default()

# //--//--//--//--//--//--//

# Логика условий для internet_green_unit

@check_call_state(nv)
def internet_green_logic(r):
    nn.log('unit', 'internet_green_unit')
    internet_green_unit_exec_count = nn.env('internet_green_unit_exec_count')
    if not internet_green_unit_exec_count:
        nn.env('internet_green_unit_exec_count', 1)
    else:
        internet_green_unit_exec_count = internet_green_unit_exec_count + 1
        nn.env('internet_green_unit_exec_count', internet_green_unit_exec_count)
        if internet_green_unit_exec_count and internet_green_unit_exec_count > 10:
            nn.log("Recursive execution detected")
            return

    if not r:
        nn.log("condition", "NULL")
        return internet_green_null()

    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        return internet_green_default()

    if r.has_entity("repeat"):
        if r.entity("repeat") == 'true':
            nn.log("condition", "repeat=True")
            return internet_green_repeat()

    if r.has_entity("robot"):
        if r.entity("robot") == 'true':
            nn.log("condition", "robot=True")
            return internet_green_robot()

    if r.has_entity("operator"):
        if r.entity("operator") == 'true':
            nn.log("condition", "operator=True")
            return goodbye_operator_demand()

    if r.has_entity("confirm"):
        if r.entity("confirm") == 'true':
            nn.log("condition", "confirm=True")
            return more_question_main()
        if r.entity("confirm") == 'false':
            nn.log("condition", "confirm=False")
            return goodbye_internet_green()

    return internet_green_default()

# //--//--//--//--//--//--//

# Логика условий для more_question_unit

@check_call_state(nv)
def more_question_logic(r):
    nn.log('unit', 'more_question_unit')
    more_question_unit_exec_count = nn.env('more_question_unit_exec_count')
    if not more_question_unit_exec_count:
        nn.env('more_question_unit_exec_count', 1)
    else:
        more_question_unit_exec_count = more_question_unit_exec_count + 1
        nn.env('more_question_unit_exec_count', more_question_unit_exec_count)
        if more_question_unit_exec_count and more_question_unit_exec_count > 10:
            nn.log("Recursive execution detected")
            return

    if not r:
        nn.log("condition", "NULL")
        return more_question_null()

    if not r.has_entities():
        nn.log('condition', 'DEFAULT')
        return more_question_default()

    if r.has_entity("payment_problem"):
        if r.entity("payment_problem") == 'true':
            nn.log("condition", "payment_problem=True")
            return payment_main()

    if r.has_entity("internet_problem"):
        if r.entity("internet_problem") == 'true':
            nn.log("condition", "internet_problem=True")
            return internet_main()

    if r.has_entity("tv_problem"):
        if r.entity("tv_problem") == 'true':
            nn.log("condition", "tv_problem=True")
            return tv_main()

    if r.has_entity("robot"):
        if r.entity("robot") == 'true':
            nn.log("condition", "robot=True")
            return more_question_robot()

    if r.has_entity("no_question"):
        if r.entity("no_question") == 'true':
            nn.log("condition", "no_question=True")
            return goodbye_main()

    if r.has_entity("operator"):
        if r.entity("operator") == 'true':
            nn.log("condition", "operator=True")
            return goodbye_operator_demand()

    if r.has_entity("confirm"):
        if r.entity("confirm") == 'true':
            nn.log("condition", "confirm=True")
            return more_question_confirm()

    return more_question_default()
