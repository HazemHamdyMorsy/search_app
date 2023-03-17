strCtime = time.ctime(os.path.getctime('-PATH-'))  # Fri Jun 07 16:54:31 2013
Cdatetime_object = datetime.strptime(strCtime, '%a %b %d %H:%M:%S %Y')
CdatetimeFormat = Cdatetime_object.strftime("%m/%d/%Y")  # 06/07/2013
if values['-CREATIONTIME-'] == CdatetimeFormat:
    results.append(f'{root}\\{file}'.replace('\\', '/'))
    window['-RESULTS-'].update(results)

strMtime = time.ctime(os.path.getmtime('-PATH-'))  # Fri Jun 07 16:54:31 2013
Mdatetime_object = datetime.strptime(strMtime, '%a %b %d %H:%M:%S %Y')
MdatetimeFormat = Mdatetime_object.strftime("%m/%d/%Y")  # 06/07/2013
if values['-MODIFIEDTIME-'] == MdatetimeFormat:
    results.append(f'{root}\\{file}'.replace('\\', '/'))
    window['-RESULTS-'].update(results

    if values['-MODIFIEDTIME-'] and values['-TERM-']:

        results.append(f'{root}\\{file}'.replace('\\', '/'))
    window['-RESULTS-'].update(results)
    print(values['-PATH-'])
    print(values['-CONTAINS-'])
    print(values['-TERM-'])
    )