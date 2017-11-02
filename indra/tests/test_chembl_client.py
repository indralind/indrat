from __future__ import absolute_import, print_function, unicode_literals
from builtins import dict, str
from indra.statements import Agent
from indra.databases import chembl_client
from indra.util import unicode_strs

vem = Agent('VEMURAFENIB', db_refs={'CHEBI': '63637', 'TEXT': 'VEMURAFENIB'})
braf = Agent('BRAF', db_refs={'HGNC': '1097', 'NCIT': 'C51194',
                              'TEXT': 'BRAF', 'UP': 'P15056'})

def test_get_inhibitions():
    stmt = chembl_client.get_inhibition(vem, braf)
    assert(stmt is not None)
    assert(unicode_strs(stmt))
    assert(len(stmt.evidence) > 5)
    for ev in stmt.evidence:
        assert(ev.pmid)
        assert(ev.annotations)
        assert(ev.source_api == 'chembl')
        assert(ev.source_id)


def test_get_all_protein_activities_vem():
    stmts = chembl_client.get_all_protein_activities(vem)
    assert(stmts is not None)
    for st in stmts:
        assert(unicode_strs(st))
        assert(len(st.evidence) >= 1)
        for ev in st.evidence:
            assert(ev.pmid)
            assert(ev.annotations)
            assert(ev.source_api == 'chembl')
            assert(ev.source_id)


