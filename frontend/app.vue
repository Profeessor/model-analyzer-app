<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Model Analyzer</h1>
    <div class="mb-4">
      <label class="block text-sm font-medium mb-1">Input Data (comma-separated numbers)</label>
      <input 
        v-model="dataInput" 
        type="text" 
        class="w-full p-2 border rounded"
        placeholder="1.5, 2.3, 4.1, 5.7"
      />
    </div>
    <button 
      @click="analyzeData" 
      class="bg-blue-500 text-white px-4 py-2 rounded"
      :disabled="isLoading"
    >
      {{ isLoading ? 'Analyzing...' : 'Analyze Data' }}
    </button>
    
    <div v-if="result" class="mt-4 p-4 border rounded bg-gray-50">
      <h2 class="font-bold">Results:</h2>
      <pre>{{ result }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const dataInput = ref('1.5, 2.3, 4.1, 5.7')
const result = ref(null)
const isLoading = ref(false)

async function analyzeData() {
  const config = useRuntimeConfig()
  isLoading.value = true
  
  try {
    // Parse comma-separated values to floats
    const data = dataInput.value.split(',').map(val => parseFloat(val.trim()))
    
    // Check for invalid data
    if (data.some(val => isNaN(val))) {
      alert('Please enter valid numbers separated by commas')
      isLoading.value = false
      return
    }
    
    // Send to backend API
    const response = await fetch(`${config.public.apiBaseUrl}/api`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        user_id: 'test-user',
        data
      })
    })
    
    result.value = await response.json()
  } catch (error) {
    console.error('Analysis error:', error)
    result.value = { error: 'Failed to analyze data' }
  } finally {
    isLoading.value = false
  }
}
</script>
