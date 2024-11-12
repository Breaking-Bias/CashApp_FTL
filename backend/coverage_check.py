if __name__ == '__main__':
    import coverage
    import pytest

    # This is the basic usage of coverage; include lists which files we
    # want the coverage report for.
    cov = coverage.Coverage()
    cov.start()

    # call your code for coverage
    pytest.main()

    cov.stop()
    cov.save()

    # generate the html report (similar to what pyTA does)
    # and print the coverage percentage

    cov_report = cov.report()

    import os
    if not os.getenv('GITHUB_ACTIONS'):
        print('test')
        cov_report = cov.html_report()
        # code below would open up the detailed report in the browser (like pyTA).
        import webbrowser

        webbrowser.open(f'file://{os.path.dirname(__file__)}/htmlcov/index.html')

    assert cov_report >= 80, f'Code coverage is below 90%: {cov_report:.2f}%'

