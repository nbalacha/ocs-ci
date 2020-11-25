import logging
import pytest

from ocs_ci.ocs import constants
from ocs_ci.framework.testlib import E2ETest, tier2


@tier2
class TestCreateNewScWithNeWRbDPoolE2EWorkloads(E2ETest):

    @pytest.mark.parametrize(
        argnames=["replica", "compression"],
        argvalues=[
            pytest.param(
                *[2, 'aggressive'], marks=pytest.mark.polarion_id("OCS-XXX")
            )
        ],
    )
    def test_new_sc_new_rbd_pool_amq(
            self,
            storageclass_factory,
            amq_factory_fixture,
            replica,
            compression):
        interface_type = constants.CEPHBLOCKPOOL
        sc_obj = storageclass_factory(
            interface=interface_type,
            new_rbd_pool=True,
            replica=replica,
            compression=compression,
        )
        self.amq, self.threads = amq_factory_fixture(sc_name=sc_obj.name)

        logging.info("Validate message run completely")
        for thread in self.threads:
            thread.result(timeout=1800)


class TestCreateNewScWithNeWRbDPoolCouchBase(E2ETest):
    @pytest.mark.parametrize(
        argnames=["replica", "compression"],
        argvalues=[
            pytest.param(
                *[2, 'aggressive'], marks=pytest.mark.polarion_id("OCS-XXX")
            )
        ],
    )
    def test_new_sc_new_rbd_pool_couchbase(
            self,
            storageclass_factory,
            couchbase_factory_fixture,
            replica,
            compression):
        interface_type = constants.CEPHBLOCKPOOL
        sc_obj = storageclass_factory(
            interface=interface_type,
            new_rbd_pool=True,
            replica=replica,
            compression=compression,
        )
        self.cb = couchbase_factory_fixture(sc_name=sc_obj.name)


class TestCreateNewScWithNeWRbDPoolPgSQL(E2ETest):

    @pytest.mark.parametrize(
        argnames=["replica", "compression"],
        argvalues=[
            pytest.param(
                *[2, 'aggressive'], marks=pytest.mark.polarion_id("OCS-XXX")
            )
        ],
    )
    def test_new_sc_new_rbd_pool_pgsql(
            self,
            storageclass_factory,
            pgsql_factory_fixture,
            replica,
            compression):
        interface_type = constants.CEPHBLOCKPOOL
        sc_obj = storageclass_factory(
            interface=interface_type,
            new_rbd_pool=True,
            replica=replica,
            compression=compression,
        )
        self.pgsql = pgsql_factory_fixture(
            replicas=3, clients=3, transactions=600, sc_name=sc_obj.name)
