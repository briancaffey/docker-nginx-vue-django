<template>
  <div class="about">
    <div v-for="(a, n) in 4" :key="n" class="chart-container">
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
        credits: {
          enabled: false,
        },
        legend: {
          itemStyle: {
              color: '#fff'
          },
          itemHoverStyle: {
              color: '#fff'
          },
          itemHiddenStyle: {
              color: '#000'
          },
        },
        borderWidth: 5,
        title: {
          style: {
            color: '#fff',
          },
        },
        yAxis: {
          labels: {
            style: {
              color: '#fff',
            },
          },
          title: {
            style: {
              color: '#fff',
            },
          },
        },
        xAxis: {
          labels: {
            style: {
              color: '#fff',
            },
          },
        },
        chart: {
          type: 'column',
          backgroundColor: '#2c3e50',
        },
        colors: ['#910000', '#1aadce', '#492970', '#f28f43', '#77a1e5', '#c42525', '#a6c96a'],
        series: [
          {
            data: this.fetchData(),
            borderColor: '#2c3e50',
          },
          {
            data: this.fetchData(),
            borderColor: '#2c3e50',
          },
        ],
      },
    };
  },
  methods: {
    fetchData() {
      return Array.from({length: 6}, () => Math.floor(Math.random() * 40));
;
    },
  },
  mounted() {
    document.title = 'Charts';
  },
};

</script>
