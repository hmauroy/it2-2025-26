gs1_country_codes = {
    (1, 19): "UPC-A compatible - United States",
    (20, 29): "UPC-A compatible - Used to issue restricted circulation numbers within a geographic region",
    (30, 39): "UPC-A compatible - United States drugs (United States National Drug Code)",
    (40, 49): "UPC-A compatible - Used to issue restricted circulation numbers within a company",
    (50, 59): "UPC-A compatible - GS1 US reserved for future use",
    (60, 99): "UPC-A compatible - United States",
    (100, 139): "United States",
    (200, 299): "Used to issue GS1 restricted circulation number within a geographic region",
    (300, 379): "France and Monaco",
    380: "Bulgaria",
    383: "Slovenia",
    385: "Croatia",
    387: "Bosnia and Herzegovina",
    389: "Montenegro",
    390: "Kosovo",
    (400, 440): "Germany",
    (450, 459): "Japan (new Japanese Article Number range)",
    (460, 469): "Russia",
    470: "Kyrgyzstan",
    471: "Taiwan",
    474: "Estonia",
    475: "Latvia",
    476: "Azerbaijan",
    477: "Lithuania",
    478: "Uzbekistan",
    479: "Sri Lanka",
    480: "Philippines",
    481: "Belarus",
    482: "Ukraine",
    483: "Turkmenistan",
    484: "Moldova",
    485: "Armenia",
    486: "Georgia",
    487: "Kazakhstan",
    488: "Tajikistan",
    489: "Hong Kong",
    (490, 499): "Japan (original Japanese Article Number range)",
    (500, 509): "United Kingdom",
    (520, 521): "Greece",
    528: "Lebanon",
    529: "Cyprus",
    530: "Albania",
    531: "North Macedonia",
    535: "Malta",
    539: "Ireland",
    (540, 549): "Belgium and Luxembourg",
    560: "Portugal",
    569: "Iceland",
    (570, 579): "Denmark, Faroe Islands and Greenland",
    590: "Poland",
    594: "Romania",
    599: "Hungary",
    (600, 601): "South Africa",
    603: "Ghana",
    604: "Senegal",
    605: "Uganda",
    606: "Angola",
    607: "Oman",
    608: "Bahrain",
    609: "Mauritius",
    611: "Morocco",
    612: "Somalia",
    613: "Algeria",
    615: "Nigeria",
    616: "Kenya",
    617: "Cameroon",
    618: "Ivory Coast",
    619: "Tunisia",
    620: "Tanzania",
    621: "Syria",
    622: "Egypt",
    623: "Managed by GS1 Global Office for future MO (was Brunei until May 2021)",
    624: "Libya",
    625: "Jordan",
    626: "Iran",
    627: "Kuwait",
    628: "Saudi Arabia",
    629: "United Arab Emirates",
    630: "Qatar",
    631: "Namibia",
    632: "Rwanda",
    (640, 649): "Finland",
    (680, 681): "China",
    (690, 699): "China",
    (700, 709): "Norway",
    729: "Israel",
    (730, 739): "Sweden",
    740: "Guatemala",
    741: "El Salvador",
    742: "Honduras",
    743: "Nicaragua",
    744: "Costa Rica",
    745: "Panama",
    746: "Dominican Republic",
    750: "Mexico",
    (754, 755): "Canada",
    759: "Venezuela",
    (760, 769): "Switzerland and Liechtenstein",
    (770, 771): "Colombia",
    773: "Uruguay",
    775: "Peru",
    777: "Bolivia",
    (778, 779): "Argentina",
    780: "Chile",
    784: "Paraguay",
    786: "Ecuador",
    (789, 790): "Brazil",
    (800, 839): "Italy, San Marino and Vatican City",
    (840, 849): "Spain and Andorra",
    850: "Cuba",
    858: "Slovakia",
    859: "Czech Republic",
    860: "Serbia",
    865: "Mongolia",
    867: "North Korea",
    (868, 869): "Turkey",
    (870, 879): "Netherlands",
    (880, 881): "South Korea",
    883: "Myanmar",
    884: "Cambodia",
    885: "Thailand",
    888: "Singapore",
    890: "India",
    893: "Vietnam",
    894: "Bangladesh",
    896: "Pakistan",
    899: "Indonesia",
    (900, 919): "Austria",
    (930, 939): "Australia",
    (940, 949): "New Zealand",
    950: "GS1 Global Office: Used to support territories & countries where no GS1 Member Organisation operates",
    951: "Used to issue General Manager Numbers for the EPC General Identifier (GID) scheme",
    952: "Used for demonstrations and examples of the GS1 system",
    955: "Malaysia",
    958: "Macau",
    (960, 9624): "GS1 UK Office: GTIN-8 allocations",
    (9625, 9626): "GS1 Poland Office: GTIN-8 allocations",
    (9627, 969): "GS1 Global Office: GTIN-8 allocations",
    977: "Serial publications (ISSN)",
    (978, 979): "Bookland (ISBN-13)",
    980: "Refund receipts",
    (981, 983): "GS1 coupon identification for common currency areas",
    (990, 999): "GS1 coupon identification"
}


def lookup_gs1_code(code):
    """
    Look up a GS-1 code and return the associated country/region.
    
    Args:
        code: Integer GS-1 code to look up
        
    Returns:
        String description of the country/region, or None if not found
    """
    # Check single codes first
    if code in gs1_country_codes:
        return gs1_country_codes[code]
    
    # Check ranges
    for key, value in gs1_country_codes.items():
        if isinstance(key, tuple) and len(key) == 2:
            start, end = key
            if start <= code <= end:
                return value
    
    return None


# Example usage
if __name__ == "__main__":
    test_codes = [5, 705, 380, 978, 890, 492, 702, 739, 400, 731, 366, 500, 704, 872, 978]
    
    for code in test_codes:
        result = lookup_gs1_code(code)
        print(f"Code {code}: {result}")