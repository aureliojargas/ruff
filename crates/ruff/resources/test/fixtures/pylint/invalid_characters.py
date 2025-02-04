# ensures language of the file is detected as English in text editors
# (Pylint, "E1206") => Rule::LoggingTooFewArgs,
#        (Pylint, "E1307") => Rule::BadStringFormatType,
#        (Pylint, "E2502") => Rule::BidirectionalUnicode,
#        (Pylint, "E2510") => Rule::InvalidCharacterBackspace,
#        (Pylint, "E2511") => Rule::InvalidCharacterCarriageReturn,
#        (Pylint, "E2512") => Rule::InvalidCharacterSub,
#        (Pylint, "E2513") => Rule::InvalidCharacterEsc,
#        (Pylint, "E2514") => Rule::InvalidCharacterNul,
#        (Pylint, "E2515") => Rule::InvalidCharacterZeroWidthSpace,
#        (Pylint, "E1310") => Rule::BadStrStripCall,
#        (Pylint, "C0414") => Rule::UselessImportAlias,
#        (Pylint, "C3002") => Rule::UnnecessaryDirectLambdaCall,
#foo = 'hi'
b = ''

b_ok = '\\b'

cr_ok = '\\r'

sub = 'sub '

sub_ok = '\x1a'

esc = 'esc esc '

esc_ok = '\x1b'

nul = '''
nul  '''

nul_ok = '\0'

zwsp = 'zero​width'

zwsp_ok = '\u200b'

zwsp_after_multibyte_character = "ಫ​"
zwsp_after_multicharacter_grapheme_cluster = "ಫ್ರಾನ್ಸಿಸ್ಕೊ ​​"
