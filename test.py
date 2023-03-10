def Test_DocParser():
    from DocParser import MyExcel
    data = {
        "Student": [
            {
                "Name": "Jack",
                "StudentId": 4,
                "Age": 5
            },
            {
                "Name": "Smith",
                "StudentId": 7,
                "Age": 8
            },
            {
                "Name": "Smit",
                "StudentId": 10,
                "Age": 11
            }
        ]
    }
    t1 = MyExcel("./test_out.xlsx")
    t1.export(data)
    print(t1.read())

    t2 = MyExcel("./test_out.csv")
    t2.export(data["Student"])
    print(t2.read())

    
if __name__ == "__main__":
    Test_DocParser()