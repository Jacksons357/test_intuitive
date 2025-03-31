<template>
  <v-container>
    <v-form @submit.prevent="handleSearch">
      <v-text-field
        v-model="search"
        label="Pesquisar"
        append-icon="mdi-magnify"
        @keydown.enter="handleSearch"
      />
    </v-form>
    <v-data-table
      :items-per-page="7"
      :headers="headers"
      :items="displayedItems"
      :loading="loading"
      item-value="name"
    >
      <template #item.data_registro_ans="{ item }">
        {{ formatDate(item.data_registro_ans) }}
      </template>
    </v-data-table>
  </v-container>
</template>

<script setup lang="ts">
import moment from 'moment';
import { ref, onMounted, computed, watch } from 'vue';
import axios from 'axios';

interface Item {
  id: number;
  data_registro_ans: string;
  registro_ans: string;
  cnpj: string;
  razao_social: string;
  nome_fantasia: string;
  modalidade: string;
  logradouro: string;
  numero: string;
  complemento: string;
  bairro: string;
  cidade: string;
  uf: string;
  cep: string;
  ddd: string;
  telefone: string;
  fax: string;
  endereco_eletronico: string;
  representante: string;
  cargo_representante: string;
  regiao_comercializacao: string;
}

const formatDate = (date: string) => {
  return moment(date).format('DD/MM/YYYY');
};

const headers = ref([
  { title: 'Registro', key: 'data_registro_ans' },
  { title: 'Reg ANS', key: 'registro_ans' },
  { title: 'CNPJ', key: 'cnpj' },
  { title: 'Rz social', key: 'razao_social' },
  { title: 'Nome Fant', key: 'nome_fantasia' },
  { title: 'Modalidade', key: 'modalidade' },
  { title: 'Lograd.', key: 'logradouro' },
  { title: 'Núm', key: 'numero' },
  { title: 'Compl.', key: 'complemento' },
  { title: 'Bairro', key: 'bairro' },
  { title: 'cidade', key: 'cidade' },
  { title: 'uf', key: 'uf' },
  { title: 'cep', key: 'cep' },
  { title: 'ddd', key: 'ddd' },
  { title: 'telefone', key: 'telefone' },
  { title: 'fax', key: 'fax' },
  { title: 'email', key: 'endereco_eletronico' },
  { title: 'representante', key: 'representante' },
  { title: 'cargo', key: 'cargo_representante' },
  { title: 'regiao', key: 'regiao_comercializacao' },
]);
const allItems = ref<Item[]>([]);
const searchResults = ref<Item[]>([]);
const loading = ref(false);
const search = ref('');

let timeoutId: number | null = null;

const displayedItems = computed(() => {
  return search.value ? searchResults.value : allItems.value;
});

const loadItems = async () => {
  loading.value = true;
  try {
    const response = await axios.get<Item[]>('http://localhost:5000/api');
    allItems.value = response.data;
  } catch (error: any) {
    console.error('Erro ao buscar dados:', error.message);
  } finally {
    loading.value = false;
  }
};

const handleSearch = async () => {
  loading.value = true;
  try {
    const response = await axios.get<Item[]>('http://localhost:5000/api/search', {
      params: { q: search.value },
    });
    if (response.data.length === 0) {
      searchResults.value = [];
    } else {
      searchResults.value = response.data;
    }
  } catch (error: any) {
    console.error('Erro ao buscar dados:', error.message);
    searchResults.value = [];
  } finally {
    loading.value = false;
  }
};


watch(search, () => {
  if (timeoutId) {
    clearTimeout(timeoutId);
  }
  timeoutId = setTimeout(() => {
    handleSearch();
    timeoutId = null;
  }, 1000);
});

onMounted(() => {
  loadItems();
});
</script>