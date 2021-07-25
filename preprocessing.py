
import language_check
from gingerit.gingerit import GingerIt



class Grammar():
    @classmethod
    def check_offline(cls, text):
        tool = language_check.LanguageTool('en-US')
        matches = tool.check(text)
        corrected = language_check.correct(text, matches)
        #corrected = text
        return corrected

    @classmethod
    def check_online(cls, text):
        parser = GingerIt()
        return parser.parse(text)['result']

    @classmethod
    def check(cls, text):
        try:
            corrected = Grammar.check_online(text)
        except Exception as e:
            corrected = Grammar.check_offline(text)
        return corrected

# init Grammar check
Grammar.check_offline('')
