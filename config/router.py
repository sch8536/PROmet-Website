from config.settings import USE_REPLICA_DATABASE
class ReplicaRouter:
	def db_for_read(self, model, **hints):
		if USE_REPLICA_DATABASE:
			return 'replica'
		return None
	def db_for_write(self, mode, **hints):
		return 'default'
	def allow_relation(self, obj1, obj2, **hints):
		db_set = {'default', 'replica'}
		if obj1._state.db in db_set and obj2._state.db in db_set:
			return True
		return None
	def allow_migrate(self, db, app_label, model_name=None,**hints):
		return True
