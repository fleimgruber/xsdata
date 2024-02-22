from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import XmlSerializer

from xsdata.iso.models import (
    CiAddress1,
    CiAddress2,
    CiContact1,
    CiContact2,
    CiIndividual2,
    CiOrganisation2,
    CiResponsibility2,
    CiResponsibleParty,
    CiRoleCode2,
    MdMetadata1,
    MdMetadata2
)

organization_name = "corp Ltd."
person_name = "John Doe"
person_email = "john.doe@johndoe.com"

context = XmlContext()
serializer = XmlSerializer(context=context)


def test_metadata2() -> None:
    metadata2 = MdMetadata2(
        contact=[
            CiResponsibility2(
                role=CiRoleCode2(value="pointOfContact"),
                party=[
                    CiOrganisation2(
                        name=organization_name,
                        individual=CiIndividual2(
                            name=person_name,
                            contact_info=CiContact2(
                                address=[CiAddress2(electronic_mail_address=[person_email])]
                            ),
                        ),
                    )
                ],
            )
        ]
    )
    print(serializer.render(metadata2))


def test_metadata1() -> None:
    metadata1 = MdMetadata1(
        contact=[
            CiResponsibleParty(
                organisation_name=organization_name,
                individual_name=person_name,
                contact_info=[CiContact1(address=[CiAddress1(electronic_mail_address=[person_email])])],
            ),
        ]
    )
    print(serializer.render(metadata1))
