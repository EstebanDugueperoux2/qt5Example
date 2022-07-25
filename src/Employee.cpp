#ifndef EMPLOYEE_H
#define EMPLOYEE_H

include <QString>
include <QDate>

class Employee
{
public:
    Employee() {}
    Employee(const QString &name, QDate dateOfBirth);

private:
    QString myName;
    QDate myDateOfBirth;
};

inline bool operator==(const Employee &e1, const Employee &e2)
{
    return e1.name() == e2.name()
           && e1.dateOfBirth() == e2.dateOfBirth();
}

inline uint qHash(const Employee &key, uint seed)
{
    return qHash(key.name(), seed) ^ key.dateOfBirth().day();
}

#endif // EMPLOYEE_H
