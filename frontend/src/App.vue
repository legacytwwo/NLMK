<template>
  <div class="main-weather">
    <div class="weather-container">
      <div class="weather-today" v-if="!loading">
        <div class="text-[24px] self-center">Moscow Weather Today</div>
        <div>
          Dayhour:
          {{ weatherTodayModel.dayhour }} 
        </div>
        <div>
          Temperature:
          {{ weatherTodayModel.temperature }} Celsius
        </div>
        <div>
          Precipitation:
          {{ weatherTodayModel.precipitation }}
        </div>
        <div>
          Humidity:
          {{ weatherTodayModel.humidity }}
        </div>
        <div>
          Wind:
          {{ weatherTodayModel.wind }} Km
        </div>
        <div>
          Comment:
          {{ weatherTodayModel.comment }}
        </div>
      </div>
      <Line v-if="!loading"
        :chart-data="chartData"
        :width="1000"
        :height="600"
      />
      <div v-if="loading">
        Loading...
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { Line } from 'vue-chartjs'
  import { onMounted, ref } from 'vue'
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js'

  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, PointElement, LineElement)

  let loading = ref(true)

  const region = ref()

  const labels = ref([])

  const max_temp = ref([])
  const min_temp = ref([])

  const weatherTodayModel = ref({
    'wind': null, 'comment': null,
    'dayhour': null, 'temperature': null,
    'precipitation': null, 'humidity': null,
  })

  const chartData = ref({
    labels: labels,
    datasets: [{
      label: 'Max Temp',
      data: max_temp,
      fill: false,
      borderColor: 'rgb(184, 25, 25)',
      tension: 0.3
    },
    {
      label: 'Min Temp',
      data: min_temp,
      fill: false,
      borderColor: 'rgb(11, 82, 189)',
      tension: 0.3
    }]
  });

  onMounted( async () => {
    let url = 'http://localhost:8000/api/weather';
    await fetch(url)
    .then(response => response.json())
    .then((response) => {
      region.value = response['region'];
      const next_days = response['next_days']
      const today = response['currentConditions']
      weatherTodayModel.value.comment = today['comment']
      weatherTodayModel.value.wind = today['wind']['km']
      weatherTodayModel.value.dayhour = today['dayhour']
      weatherTodayModel.value.humidity = today['humidity']
      weatherTodayModel.value.precipitation = today['precip']
      weatherTodayModel.value.temperature = today['temp']['c']
      next_days.forEach(element => {
        labels.value.push(element['day'])
        max_temp.value.push(element['max_temp']['c'])
        min_temp.value.push(element['min_temp']['c'])
      });
    })
    loading.value = false
  })

</script>

<style lang="scss" scoped>
  @import "./App.scss";
</style>