from django.db import models


class Address(models.Model):
    teryt = models.IntegerField(default=0)
    number_of_district = models.IntegerField(default=0)
    address = models.CharField(max_length=500, default=None)
    district = models.CharField(max_length=50, default=None)
    commune = models.CharField(max_length=200, default=None)
    commune_type = models.CharField(max_length=200, default=None)
    county = models.CharField(max_length=200, default=None)
    voivodeship = models.CharField(max_length=200, default=None)
    number_of_electoral_circuit = models.IntegerField(default=0)
    number_electoral_circuits = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Votes_data(Address):
    type = models.CharField(max_length=10, default=None)
    number_of_voters = models.IntegerField(default=0)
    number_of_proxies = models.IntegerField(default=0)
    cards_given = models.IntegerField(default=0)
    cards_taken = models.IntegerField(default=0)
    cards_taken_from_box = models.IntegerField(default=0)
    votes_valid = models.IntegerField(default=0)
    votes_invalid = models.IntegerField(default=0)
    cards_received = models.IntegerField(default=0)
    cards_valid = models.IntegerField(default=0)
    cards_invalid = models.IntegerField(default=0)
    cards_invalid_x = models.IntegerField(default=0)
    cards_invalid_xx = models.IntegerField(default=0)
    cards_unused = models.IntegerField(default=0)
    polish_citizens = models.IntegerField(default=0)
    polish_citizens_b = models.IntegerField(default=0)
    envelope_unsealed = models.IntegerField(default=0)
    envelopes_thrown_into_box = models.IntegerField(default=0)
    envelopes_without_statement = models.IntegerField(default=0)
    envelopes_returned = models.IntegerField(default=0)
    envelopes_returned_without_envelope = models.IntegerField(default=0)
    unsigned_statements = models.IntegerField(default=0)
    eu_citizens = models.IntegerField(default=0)
    eu_citiznes_b = models.IntegerField(default=0)
    electoral_packages = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Election(Votes_data):
    election_type = models.CharField(max_length=10, default=None)
    votes = models.CharField(max_length=10000, default=None)


class Candidate(models.Model):
    surname = models.CharField(max_length=255, default=None)
    names = models.CharField(max_length=255, default=None)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=3, default=None)
    place_of_living = models.CharField(max_length=511, default=None)
    voivodeship = models.CharField(max_length=127, default=None)
    nationality = models.CharField(max_length=127, default=None)
    votes = models.IntegerField(default=0)
    election_committee = models.CharField(max_length=63, default=None)  # coded, i.e 'kw1', 'kwp2'
    number_of_list = models.IntegerField(default=0)
    pos = models.IntegerField(default=0)
    number_of_district = models.IntegerField(default=0)
    grade = models.CharField(max_length=10, default=None)
    teryt = models.IntegerField(default=0)
