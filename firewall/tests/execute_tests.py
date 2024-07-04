def execute_tests(name, list_of_tests):
    # tests to pass
    print(f'\n[+] Starting tests for {name}')
    print(f'\n[+] The following tests must be passed:')
    for test in list_of_tests[0]:
        test()
    print(f'\n[+] The following tests must NOT be passed:')
    for test in list_of_tests[1]:
        test()