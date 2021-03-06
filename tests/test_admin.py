from datetime import datetime
from app.models.types import TypeLinks, TypeNews
from app.models.links import Link


def test_res200(client):
    res = client.get('/admin/')
    print(res.response._callbacks)
    assert res.status_code == 200


def test_res200_tnews(client):
    res = client.get('/admin/type/news')
    assert res.status_code == 200

    res = client.get('/admin/type?tab=news')
    assert res.status_code == 200

    res = client.post('/admin/type/news',
                      data={'addtype': ''},
                      follow_redirects=True)
    assert res.status_code == 200


def test_res200_tlinks(client):
    res = client.get('/admin/type/links')
    assert res.status_code == 200

    res = client.get('/admin/type?tab=links')
    assert res.status_code == 200

    res = client.post('/admin/type/links',
                      data={'addtype': ''},
                      follow_redirects=True)
    assert res.status_code == 200


def test_res200_links(client):
    res = client.get('/admin/links')
    assert res.status_code == 200

    res = client.post('/admin/links',
                      data={'addlink': ''},
                      follow_redirects=True)
    assert res.status_code == 200

    res = client.get('/admin/links/link')
    assert res.status_code == 200

    res = client.get('/admin/links/get_links')
    assert res.status_code == 200


def test_dbtable_tnews(client):
    res = client.post('/admin/type?tab=news',
                      data={'typename': 'new',
                            'typecode': 1,
                            'isactive': True},
                      follow_redirects=True)
    assert res.status_code == 200

    item = TypeNews.get_by_id(1)
    assert item is not None

    res = client.post('/admin/type/news',
                      data={'changesub': '1'},
                      follow_redirects=True)
    assert res.status_code == 200

    res = client.get('/admin/type?id=1&tab=news')
    assert res.status_code == 200

    res = client.post('/admin/type/news',
                      data={'delsub': '1'},
                      follow_redirects=True)
    assert res.status_code == 200


def test_dbtable_tlinks(client):
    res = client.post('/admin/type?tab=links',
                      data={'typename': 'new',
                            'typecode': 1,
                            'isactive': True},
                      follow_redirects=True)
    assert res.status_code == 200

    item = TypeLinks.get_by_id(1)
    assert item is not None

    res = client.post('/admin/type/links',
                      data={'changesub': '1'},
                      follow_redirects=True)
    assert res.status_code == 200

    res = client.get('/admin/type?id=1&tab=links')
    assert res.status_code == 200

    res = client.post('/admin/type/links',
                      data={'delsub': '1'},
                      follow_redirects=True)
    assert res.status_code == 200


def test_dbtable_links(client):
    res = client.post('/admin/links/link',
                      data={'linkname': 'new',
                            'fullname': 'new',
                            'typelink': 1,
                            'user': 1,
                            'position': 0,
                            'createdate': datetime.today(),
                            'changedate': datetime.today(),
                            'isactive': True},
                      follow_redirects=True)
    assert res.status_code == 200

    item = Link.get_by_id(1)
    assert item is not None

    res = client.post('/admin/links',
                      data={'changesub': '1'},
                      follow_redirects=True)
    assert res.status_code == 200

    res = client.get('/admin/links/link?id=1')
    assert res.status_code == 200

    res = client.post('/admin/links',
                      data={'delsub': '1'},
                      follow_redirects=True)
    assert res.status_code == 200
