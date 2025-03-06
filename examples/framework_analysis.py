
import math as m
import random

from itertools import chain

import matplotlib.pyplot as plt

from sentinelpricing import Framework, LookupTable, TestSuite, TestCase


def generate_random_testcase():
	return {
		"age": round(random.gammavariate(5, 45 / 5)),
		"lic": 9 - round(random.expovariate(0.8))
	}


age_rates = [
	{"age": a, "rate": 1.5 * max((17/a),0.8)}
	for a in chain([17,], range(20, 80, 15))
]

lic_rates = [
	{"lic": l, "rate": max(1 - (l * 0.2), 0.8)}
	for l in range(0,8)
]

proposed_age_rates = [
	{"age": a, "rate": 1.4 * max((17/a),0.75)}
	for a in chain([17,], range(20, 80, 1))
]


testcases = TestSuite(
	[
		TestCase(
			generate_random_testcase()
		)
		for _ in range(10_000)
	]
)


class MotorV1(Framework):
	def setup(self):
		self.age = LookupTable(age_rates)
		self.lic = LookupTable(lic_rates)

	def calculation(self, quote):
		age_rate = self.age[quote['age']]
		lic_rate = self.lic[quote['lic']]

		quote += 400
		quote *= age_rate
		quote *= lic_rate

		return quote

class MotorV2(MotorV1):
	def setup(self):
		self.age = LookupTable(proposed_age_rates)
		self.lic = LookupTable(lic_rates)


current = MotorV1.quote_many(testcases)
proposed = MotorV2.quote_many(testcases)

avg_final_price_by_age = current.avg(
	by="age", bins=lambda x: m.floor(x / 10) * 10
)

proposed_avg_final_price_by_age = proposed.avg(
	by="age", bins=lambda x: m.floor(x / 10) * 10
)

for key in avg_final_price_by_age.keys():
	print(key, round(avg_final_price_by_age[key],2), ">>", round(proposed_avg_final_price_by_age[key],2))

fig, ax = plt.subplots()

ax.plot(avg_final_price_by_age.keys(), avg_final_price_by_age.values())
ax.plot(proposed_avg_final_price_by_age.keys(), proposed_avg_final_price_by_age.values())

plt.show()
