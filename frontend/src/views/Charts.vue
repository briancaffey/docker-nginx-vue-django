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
      legend: {
        navigation: {
          activeColor: '#fff',
        },
        itemStyle: {
          color: '#fff',
        },
      },
      labels: {
        style: {
          color: '#ff',
        },
      },
      chartOptions: {
        borderWidth: 0,
        credits: {
          enabled: false,
        },
        title: {
          style: {
            color: '#fff',
          },
        },
        chart: {
          xAxis: {
            labels: {
              style: {
                color: '#fff',
              },
            },
          },
          type: 'bar',
          backgroundColor: '#2c3e50',
        },
        colors: ['#910000', '#1aadce', '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
        series: [
          {
            data: this.fetchData(),
            name: 'Hmm',
          },
          {
            data: this.fetchData(),
          },
        ],
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
