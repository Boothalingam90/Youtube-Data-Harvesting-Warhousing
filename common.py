class commonfunctions:
    def getValuesfromDictionary(self, data, values):
        if not data or data == "":
            return ""
        
        output = data
        for item in values.split(","):
            if item in output:
                output = output[item]
            else:
                output = ""
        return output