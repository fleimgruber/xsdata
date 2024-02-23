from pathlib import Path

import xmlschema

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from xsdata.iso.models import *

organization_name = "corp Ltd."
person_name = "John Doe"
person_email = "john.doe@johndoe.com"

context = XmlContext()
config = SerializerConfig(pretty_print=True)
serializer = XmlSerializer(context=context, config=config)


def build_schema():
    iso19115_3_mds_2_path = (
        Path("xsdata") / "schemas" / "XML" / "schemas.isotc211.org" / "19115" / "-3" / "mds" / "2.0"
    )

    sources = [
        iso19115_3_mds_2_path / "mds.xsd",
    ]

    return xmlschema.XMLSchema(sources)


class Metadata2:
    @staticmethod
    def responsibility(role: str = "pointOfContact", party: str = organization_name):
        return AbstractResponsibilityPropertyType(
            standards_iso_org_iso_19115_3_cit_2_0_ci_responsibility=CiResponsibility1(
                role=CiRoleCodePropertyType1(
                    ci_role_code=CiRoleCode1(
                        value=role,
                        code_list="codeListLocation#CI_RoleCode",
                        code_list_value=role,
                    )
                ),
                party=[
                    AbstractCiPartyPropertyType1(
                        ci_organisation=CiOrganisation1(name=CharacterStringPropertyType1(character_string=party))
                    ),
                ],
            )
        )

    @staticmethod
    def default_locale():
        return PtLocalePropertyType1(
            pt_locale=PtLocale1(
                language=LanguageCodePropertyType1(
                    language_code=LanguageCode1(
                        code_list_value="eng",
                        code_list="http://www.loc.gov/standards/iso639-2/",
                    )
                ),
                character_encoding=MdCharacterSetCodePropertyType1(
                    md_character_set_code=MdCharacterSetCode1(
                        code_list_value="utf8",
                        code_list="http://standards.iso.org/iso/19115/resources/Codelists/cat/codelists.xml#MD_CharacterSetCode",
                    )
                ),
            )
        )

    @staticmethod
    def date_info(date: tuple = (2014, 4, 3, 16, 0, 0), date_type="creation"):
        return (
            [
                AbstractTypedDatePropertyType(
                    standards_iso_org_iso_19115_3_cit_2_0_ci_date=CiDate1(
                        date=DatePropertyType1(date_time=XmlDateTime(*date)),
                        date_type=CiDateTypeCodePropertyType1(
                            ci_date_type_code=CiDateTypeCode1(
                                value=date_type,
                                code_list="codeListLocation#CI_DateTypeCode",
                                code_list_value=date_type,
                            )
                        ),
                    )
                ),
            ],
        )


def test_metadata_date_info() -> None:
    md = Metadata2()

    metadata = MdMetadata2(
        contact=[md.responsibility(party=organization_name)],
        default_locale=md.default_locale(),
        date_info=md.date_info(),
    )
    print(serializer.render(metadata))

    schema = build_schema()
    schema.validate(serializer.render(metadata))
