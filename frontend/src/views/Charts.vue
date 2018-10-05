<template>
  <div class="about">
    <div v-for="(a, n) in 2" :key="n" class="chart-container">
      <highcharts :options="chartOptions"/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Documents',
  data() {
    return {
      chartOptions: {
        series: [{
          data: this.fetchData(),
        }],
      },
    };
  },
  methods: {
    fetchData() {
      return [1, 2, 3];
    },
  },
  mounted() {
    document.title = 'Charts';
  },
};

</script>
