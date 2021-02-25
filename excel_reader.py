import pandas as pd


class ReadEx:
    try:
        lltrsDf = pd.read_excel('./BD_EX.xls', sheet_name='LLT-RS EX')
    except:
        print("OS is not Linux")
    try:
        lltrsDf = pd.read_excel('.\BD_EX.xls', sheet_name='LLT-RS EX')
    except:
        print("OS is not Windows")
    # print(lltrsDf)

    # UID LGB , LLT-MS EX , LLT-RS EX
    def lltrs_df_get(self):
        return self.lltrsDf

    def parameters_counter(self):
        comboboxesNeed = 1
        for i in range(len(self.lltrsDf)):
            counter_x = self.lltrsDf.iloc[i, 0]
            if counter_x == 'X':
                comboboxesNeed += 1
            elif counter_x:
                pass
            else:
                pass
        return comboboxesNeed


excelRead = ReadEx()
# print(excelRead.parameters_counter())

