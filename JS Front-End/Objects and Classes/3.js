function createCity(name, population, treasury) {
	return {
		name,
		population,
		treasury,
		taxRate: 10,
		collectTaxes() {
			this.treasury += this.population * this.taxRate;
		},
		applyGrowth(percantage) {
			this.population += this.population * (percantage / 100);
		},
		applyRecession(percantage) {
			this.treasury = this.treasury - this.treasury * (percantage / 100);
		},
	};
}

const city = createCity("Tortuga", 7000, 15000);
city.collectTaxes();
console.log(city.treasury);
city.applyGrowth(5);
console.log(city.population);
