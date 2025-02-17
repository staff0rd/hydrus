
from hydrus.core.interfaces import HydrusThreadingInterface

class HydrusControllerInterface( object ):
    
    def pub( self, topic, *args, **kwargs ) -> None:
        
        raise NotImplementedError()
        
    
    def pubimmediate( self, topic, *args, **kwargs ) -> None:
        
        raise NotImplementedError()
        
    
    def sub( self, object, method_name, topic ) -> None:
        
        raise NotImplementedError()
        
    
    def AcquireThreadSlot( self, thread_type ) -> bool:
        
        raise NotImplementedError()
        
    
    def ThreadSlotsAreAvailable( self, thread_type ) -> bool:
        
        raise NotImplementedError()
        
    
    def CallLater( self, initial_delay, func, *args, **kwargs ) -> HydrusThreadingInterface.SchedulableJobInterface:
        
        raise NotImplementedError()
        
    
    def CallRepeating( self, initial_delay, period, func, *args, **kwargs ) -> HydrusThreadingInterface.SchedulableJobInterface:
        
        raise NotImplementedError()
        
    
    def CallToThread( self, callable, *args, **kwargs ) -> None:
        
        raise NotImplementedError()
        
    
    def CallToThreadLongRunning( self, callable, *args, **kwargs ) -> None:
        
        raise NotImplementedError()
        
    
    def CleanRunningFile( self ) -> None:
        
        raise NotImplementedError()
        
    
    def ClearCaches( self ) -> None:
        
        raise NotImplementedError()
        
    
    def CurrentlyIdle( self ) -> bool:
        
        raise NotImplementedError()
        
    
    def CurrentlyPubSubbing( self ) -> bool:
        
        raise NotImplementedError()
        
    
    def DBCurrentlyDoingJob( self ) -> bool:
        
        raise NotImplementedError()
        
    
    def DoingFastExit( self ) -> bool:
        
        raise NotImplementedError()
        
    
    def GetBootTime( self ) -> int:
        
        raise NotImplementedError()
        
    
    def GetDBDir( self ) -> str:
        
        raise NotImplementedError()
        
    
    def GetDBStatus( self ):
        
        raise NotImplementedError()
        
    
    def GetCache( self, name ):
        
        raise NotImplementedError()
        
    
    def GetManager( self, name ):
        
        raise NotImplementedError()
        
    
    def GetTimestamp( self, name: str ) -> int:
        
        raise NotImplementedError()
        
    
    def GoodTimeToStartBackgroundWork( self ) -> bool:
        
        raise NotImplementedError()
        
    
    def GoodTimeToStartForegroundWork( self ) -> bool:
        
        raise NotImplementedError()
        
    
    def JustWokeFromSleep( self ):
        
        raise NotImplementedError()
        
    
    def IsFirstStart( self ):
        
        raise NotImplementedError()
        
    
    def LastShutdownWasBad( self ):
        
        raise NotImplementedError()
        
    
    def MaintainDB( self, maintenance_mode = None, stop_time = None ):
        
        raise NotImplementedError()
        
    
    def MaintainMemoryFast( self ):
        
        raise NotImplementedError()
        
    
    def MaintainMemorySlow( self ):
        
        raise NotImplementedError()
        
    
    def PrintProfile( self, summary, profile_text = None ):
        
        raise NotImplementedError()
        
    
    def PrintQueryPlan( self, query, plan_lines ):
        
        raise NotImplementedError()
        
    
    def Read( self, action, *args, **kwargs ):
        
        raise NotImplementedError()
        
    
    def RecordRunningStart( self ):
        
        raise NotImplementedError()
        
    
    def ReleaseThreadSlot( self, thread_type ):
        
        raise NotImplementedError()
        
    
    def ReportDataUsed( self, num_bytes ):
        
        raise NotImplementedError()
        
    
    def ReportRequestUsed( self ):
        
        raise NotImplementedError()
        
    
    def ResetIdleTimer( self ) -> None:
        
        raise NotImplementedError()
        
    
    def SetDoingFastExit( self, value: bool ) -> None:
        
        raise NotImplementedError()
        
    
    def SetTimestamp( self, name: str, value: int ) -> None:
        
        raise NotImplementedError()
        
    
    def ShouldStopThisWork( self, maintenance_mode, stop_time = None ) -> bool:
        
        raise NotImplementedError()
        
    
    def SleepCheck( self ) -> None:
        
        raise NotImplementedError()
        
    
    def SimulateWakeFromSleepEvent( self ) -> None:
        
        raise NotImplementedError()
        
    
    def SystemBusy( self ) -> bool:
        
        raise NotImplementedError()
        
    
    def TouchTimestamp( self, name: str ) -> None:
        
        raise NotImplementedError()
        
    
    def WaitUntilDBEmpty( self ) -> None:
        
        raise NotImplementedError()
        
    
    def WaitUntilModelFree( self ) -> None:
        
        raise NotImplementedError()
        
    
    def WaitUntilPubSubsEmpty( self ) -> None:
        
        raise NotImplementedError()
        
    
    def WakeDaemon( self, name ) -> None:
        
        raise NotImplementedError()
        
    
    def Write( self, action, *args, **kwargs ):
        
        raise NotImplementedError()
        
    
    def WriteSynchronous( self, action, *args, **kwargs ):
        
        raise NotImplementedError()
        
    
