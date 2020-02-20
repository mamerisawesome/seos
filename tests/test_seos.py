def test_extract_sheet_id_not_set():
    from seos import Seos
    extractor = Seos(credentials_file="./credentials.json")

    # start extraction
    extractor.sheet_name = "ProductList"
    extractor.scope = "A2:D2"
    data = extractor.extract()

    assert data == None

def test_extract_sheet_name_not_set():
    from seos import Seos
    extractor = Seos(
        credentials_file="./credentials.json",
        spreadsheet_id="1q8H07VQKftV94Sw_DQVD0z29032Iq8nuhBlaaeBYAMc"
    )

    # start extraction
    extractor.scope = "A2:D2"
    data = extractor.extract()

    assert data == None

def test_extract_scope_not_set():
    from seos import Seos
    extractor = Seos(
        credentials_file="./credentials.json",
        spreadsheet_id="1q8H07VQKftV94Sw_DQVD0z29032Iq8nuhBlaaeBYAMc"
    )

    # start extraction
    extractor.sheet_name = "ProductList"
    data = extractor.extract()

    assert data == None

def test_extract_empty_data():
    from seos import Seos
    extractor = Seos(
        credentials_file="./credentials.json",
        spreadsheet_id="1q8H07VQKftV94Sw_DQVD0z29032Iq8nuhBlaaeBYAMc"
    )

    # start extraction
    extractor.sheet_name = "NonExistentSheet"
    extractor.scope = "A:A"
    data = extractor.extract()

    assert data == []

def test_extract_data():
    from seos import Seos
    extractor = Seos(
        credentials_file="./credentials.json",
        spreadsheet_id="1q8H07VQKftV94Sw_DQVD0z29032Iq8nuhBlaaeBYAMc"
    )

    # start extraction
    extractor.sheet_name = "ProductList"
    extractor.scope = "A2:D2"
    data = extractor.extract()

    assert data == [[
        "Alisha Solid Women's Cycling Shorts",
        (
            "Key Features of Alisha Solid Women's Cycling Shorts Cotton "
            "Lycra Navy, Red, Navy,Specifications of Alisha Solid Women's "
            "Cycling Shorts Shorts Details Number of Contents in Sales "
            "Package Pack of 3 Fabric Cotton Lycra Type Cycling Shorts "
            "General Details Pattern Solid Ideal For Women's Fabric Care "
            "Gentle Machine Wash in Lukewarm Water, Do Not Bleach "
            "Additional Details Style Code ALTHT_3P_21 In the Box 3 shorts"
        ),
        "999.00",
        "411"
    ]]


def test_extract_data_on_multiple_sheets():
    from seos import Seos
    extractor = Seos(
        credentials_file="./credentials.json",
        spreadsheet_id="1q8H07VQKftV94Sw_DQVD0z29032Iq8nuhBlaaeBYAMc"
    )

    # start extraction
    extractor.sheet_name = "ProductList"
    extractor.scope = "A2:D2"
    data = extractor.extract()

    assert data == [[
        "Alisha Solid Women's Cycling Shorts",
        (
            "Key Features of Alisha Solid Women's Cycling Shorts Cotton "
            "Lycra Navy, Red, Navy,Specifications of Alisha Solid Women's "
            "Cycling Shorts Shorts Details Number of Contents in Sales "
            "Package Pack of 3 Fabric Cotton Lycra Type Cycling Shorts "
            "General Details Pattern Solid Ideal For Women's Fabric Care "
            "Gentle Machine Wash in Lukewarm Water, Do Not Bleach "
            "Additional Details Style Code ALTHT_3P_21 In the Box 3 shorts"
        ),
        "999.00",
        "411"
    ]]

    extractor.sheet_name = "JobVacancies"
    extractor.scope = "A3:B3"
    data = extractor.extract()

    assert data == [[
        "Android Developer",
        (
            "The Android Developer is responsible for developing applications "
            "for devices powered by the Android operating system."
        )
    ]]
